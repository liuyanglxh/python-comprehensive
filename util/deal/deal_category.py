import json, os

from util import file_util, mysql_local, my_json

local_file = '/Users/liuyang/tech/dm/deal/category.txt'

cache = {}
id, parent_id, label_en, label_cn, title_en, title_cn = 'id', 'parent_id', 'label_en', 'label_cn', 'title_en', 'title_cn'

"""
折扣分类缓存
"""


def init():
	"""
	初始化缓存
	"""

	if not os.path.exists(local_file):
		print("nofile")
		return

	global cache

	def func(line):
		row = json.loads(line)
		cache[int(row['id'])] = row

	file_util.read_file(local_file, func)

	print("一共[", len(cache), "]条分类信息")


def refresh():
	"""
	重新加载数据到本地
	"""
	sql = "select id, parent_id, label_en, label_cn,title_en, title_cn from category"
	db = 'dealmoon'
	data_list = []
	for x in mysql_local.execute_sql(sql, db):
		id, parent_id, label_en, label_cn, title_en, title_cn = x
		j = {
			"id": id,
			"parent_id": parent_id,
			"label_en": label_en,
			"laben_cn": label_cn,
			"title_en": title_en,
			"title_cn": title_cn
		}
		data_list.append(my_json.dumps(j))
	file_util.cover(local_file, data_list)


init()


def get(category_id: int):
	if category_id is None: return {}
	return cache.get(category_id)


def get_attr(category_id: int, attr: str):
	"""
	获取分类字段
	:param category_id:
	:param attr:
	:return:
	"""
	if category_id is None: return ""
	return cache.get(category_id).get(attr) if category_id in cache else ""


def get_attr_in_order(category_id: int, order=None):
	"""
	按顺序获取分类字段
	:param category_id:
	:param order:
	:return:
	"""
	if order is None: order = [label_cn, title_cn, label_en, title_en]
	if category_id is None: return ""
	c = cache.get(category_id)
	if not c:
		return ""
	for x in order:
		if c.get(x):
			return c.get(x)


def get_priority():
	"""
	运营比较关心的分类（参考）
	"""
	return ['美妆护肤', '电子电脑', '服饰手袋', '家居厨卫', '食品', '男士专区']


def get_all():
	return cache.values()


if __name__ == '__main__':
	for x in get_all():
		if x[title_en] != x[label_en]:    print(x[title_en], '----------', x[label_en])
