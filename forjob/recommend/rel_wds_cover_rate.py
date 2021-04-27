import json
import os
import time

from util import my_json, file_util
from util import mysql_local as mysql
from util import number_util

"""
https://www.tapd.cn/36055941/prong/stories/view/1136055941001005588
取出近两周内的有效折扣及其tag

统计：
	总1000个折扣   900个有tag，100个无tag
	覆盖率90%
	
	扩展前：平均每个折扣有？个tag
	扩展后（品牌）：平均每个折扣有？个tag（需要去重）
	扩展后（产品）：平均每个折扣有？个tag（需要去重）
"""

round_num = 2


def __tmp_dir__():
	return "/tmp/rec/rel/"


def __tmp_deal_info_path__():
	return __tmp_dir__() + "deal_info.txt"


def __word_files__():
	return ['brand_relwds.csv', 'product_relwds.csv']


def __get_name__(algorithm):
	return {
		'brand_relwds': '品牌词',
		'product_relwds': '产品词'
	}.get(algorithm)


def __recent_valid_deals__():
	"""
	从本地读取折扣tag信息，如果没有，就从mysql读
	:return	结构如下
	{
		100:{
			"is_hot":True,
			"tags":["lining","anta"]
		},
		200:{
			"is_hot":True,
			"tags":["lining","man"]
		}
	}
	"""
	if os.path.exists(__tmp_deal_info_path__()):
		info_d = {}

		def func(line):
			js = json.loads(line)
			info_d[int(js['id'])] = js['info']

		file_util.read_file(__tmp_deal_info_path__(), func)
		return __check_deal_info__(info_d)

	info_d = __read_from_db__()
	data = []
	for deal_id, info in info_d.items():
		d = {'id': deal_id, 'info': info}
		l = my_json.dumps(d)
		data.append(l)
	file_util.cover(__tmp_deal_info_path__(), data)

	return __check_deal_info__(info_d)


def __check_deal_info__(deal_info_dd):
	to_rm = []
	for deal_id, deal_info in deal_info_dd.items():
		if 'tags' not in deal_info:
			print(deal_id, '没有提取到tag')
			to_rm.append(deal_id)
		else:
			deal_info['tags'] = [tag for tag in deal_info['tags'] if tag != 'NOTAG']
	for x in to_rm: del deal_info_dd[x]
	return deal_info_dd


def __rel_tags__():
	# 读取相关tag信息
	rel_d, cur = {}, ""

	def func(line):
		rel_d.setdefault(cur, {})
		splt = line.split("\t")
		rel_d[cur][splt[0]] = splt[1].strip().split(';')

	for filename in __word_files__():
		cur = __get_name__(filename.split(".")[0])
		path = __tmp_dir__() + filename
		file_util.read_file(path, func)

	return rel_d


def __read_from_db__():
	"""
	从mysql读取折扣tag信息
	"""
	deal_sql_format = """
	SELECT id,is_hotpick
	favorite_num,comment_num,share_num,published_time
	FROM deal_index
	where published_time > %s and dead_time > %s  and id > %s
	and cn_state='published' and show_on_homepage = 1
	ORDER BY id ASC limit %s
	"""
	tag_sql_format = """
	select docid,text_tags from recon_doc_tags_deal where docid in (%s)
	"""
	batch_size = "1000"
	deal_info_d = {}
	last_id = 0
	minPublishTime, minExpireTime = int(time.time()) - 14 * 24 * 60 * 60, int(time.time())
	while True:
		deal_sql = deal_sql_format % (str(minPublishTime), str(minExpireTime), str(last_id), batch_size)
		print('deal_sql', deal_sql)
		lst = mysql.execute_sql(deal_sql, 'dealmoon')
		if len(lst) == 0: break
		print('deal num', len(lst))

		deal_ids = []
		for x in lst:
			deal_id = int(x[0])
			last_id = max(last_id, deal_id)
			deal_ids.append(str(deal_id))
			deal_info_d[deal_id] = {'is_hot': x[1] == 1}

		tag_sql = tag_sql_format % ",".join(deal_ids)
		for x in mysql.execute_sql(tag_sql, 'recdb'):
			deal_id, tags = int(x[0]), json.loads(x[1])
			if deal_id in deal_info_d:
				deal_info_d[deal_id]['tags'] = tags

	return deal_info_d


def __stats__(deal_info_DD, rel_DD):
	"""
	:param deal_info_DD: 	折扣信息
	:param rel_DD: 			扩展词信息
	"""
	# 折扣总数，有tag的折扣总数，所有折扣加起来的tag总数
	deal_num, with_tags, tags_total = len(deal_info_DD), 0, 0
	deal_tags_lst = []  # 每条折扣的tag
	for deal_info in deal_info_DD.values():
		if len(deal_info['tags']) == 0: continue
		deal_tags_lst.append(deal_info['tags'])
		with_tags += 1
		tags_total += len(deal_info['tags'])
	with_tags_rate = number_util.percent(with_tags, deal_num)
	avg_tags_num = number_util.divide(tags_total, len(deal_tags_lst), round_num)

	# 折扣扩展情况，产品词+品牌词合在一起
	tag_inr_d, both_rel_tags_d = {}, {}
	# 计算扩展后，平均每个折扣的tag数量增加了多少
	for name, rel_d in rel_DD.items():
		tag_inr_d[name] = __do_rel_stats__(deal_tags_lst, rel_d)
		for tag, rel_tags in rel_d.items():
			both_rel_tags_d.setdefault(tag, [])
			s = set()
			for x in both_rel_tags_d[tag]: s.add(x)
			for x in rel_tags: s.add(x)
			both_rel_tags_d[tag] = [x for x in s]

	tag_inr_d['品牌词+产品词'] = __do_rel_stats__(deal_tags_lst, both_rel_tags_d)

	return with_tags_rate, avg_tags_num, tag_inr_d


def __do_rel_stats__(deal_tags_LST, rel_dd):
	"""
	计算某一种算法对折扣tag的增加量
	"""
	incr_total, last_total = 0, 0
	for tags in deal_tags_LST:
		incr_tags = set()  # 扩展出来的词
		for tag in tags:
			if not tag in rel_dd: continue
			for rel_tag in rel_dd[tag]:
				incr_tags.add(rel_tag)
		incr_total += len(incr_tags)
		for tag in tags: incr_tags.add(tag)
		last_total += len(incr_tags)

	return {
		'平均每个折扣能够扩展': number_util.divide(incr_total, len(deal_tags_LST), round_num),
		'扩展后，每个折扣平均tag数': number_util.divide(last_total, len(deal_tags_LST), round_num)
	}


def __stats_deal_tag__(deal_info_ddd):
	deal_num = len(deal_info_ddd)
	tag_num = 0
	for deal_info in deal_info_ddd.values():
		tags = deal_info['tags']
		l = len(tags)
		tag_num += l
	return round(float(tag_num) / float(deal_num), 0)


if __name__ == '__main__':
	# 读取折扣相关信息
	deal_info_d = __recent_valid_deals__()
	# 读取相关tag信息
	rel_d = __rel_tags__()
	# 分析匹配情况
	with_tags_RATE, avg_tags_NUM, tag_inr_D = __stats__(deal_info_d, rel_d)
	print(my_json.dumps({
		'折扣总数': len(deal_info_d),
		'折扣tag覆盖率': with_tags_RATE,
		'平均每个折扣tag数': avg_tags_NUM,
		'扩展后': tag_inr_D
	}))
