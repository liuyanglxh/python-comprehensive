import json
import time

from forjob.deal import deal_category as category
from util import mysql_local, my_json, file_util, csv_util

tmp_file = '/tmp/deal_tmp.txt'

deal_analysis_file = '/Users/liuyang/Downloads/近2周内的折扣统计.csv'


def to_local():
	now = int(time.time())

	sql = 'select id, category, is_hotpick from deal_index where published_time >= %s and dead_time >= %s' % (
		str(now - 7 * 24 * 60 * 60), str(now))
	db = 'dealmoon'

	data_list = []
	for x in mysql_local.execute_sql(sql, db):
		id, category, is_hotpick = x
		d = {
			'id': id,
			'category': category,
			'is_hotpick': is_hotpick
		}
		data_list.append(my_json.dumps(d))

	file_util.cover(path=tmp_file, data=data_list)


def analysis():
	all_deals = []

	def func(line):
		d = json.loads(line)
		all_deals.append(d)

	file_util.read_file(tmp_file, func)

	no_category, nocategory_hot = 0, 0
	# 折扣分类统计， 热门折扣分类统计
	category_percent, category_hot_percent = {"name": "有效折扣"}, {"name": "有效热门折扣"}
	hot_total = 0
	for deal in all_deals:
		# 统计总数
		if int(deal['is_hotpick']) == 1: hot_total += 1

		# 没有分类
		if not deal.get('category'):
			no_category += 1
			if int(deal['is_hotpick']) == 1: nocategory_hot += 1
			continue

		has_category = False
		for y in deal['category'].split(','):
			category_id = top_category(int(y))
			label_cn = category.get_attr_in_order(category_id)
			if label_cn:
				has_category = True
			else:
				continue
			# 折扣统计
			category_percent.setdefault(label_cn, 0)
			category_percent[label_cn] += 1
			# 热门折扣统计
			if int(deal['is_hotpick']) == 1:
				category_hot_percent.setdefault(label_cn, 0)
				category_hot_percent[label_cn] += 1

		if not has_category:
			print("分类有问题", deal.get('id'), deal['category'])
			no_category += 1
			if int(deal['is_hotpick']) == 1:
				nocategory_hot += 1

	category_percent['无分类'] = no_category
	category_hot_percent['无分类'] = nocategory_hot
	category_percent['总数'] = len(all_deals)
	category_hot_percent['总数'] = hot_total

	title = ['name', '总数']
	for k in category_percent:
		if k not in title:
			title.append(k)

	print(category_percent)
	print(category_hot_percent)

	csv_util.cover(deal_analysis_file, title, [category_percent, category_hot_percent])


def top_category(category_id) -> int:
	while True:
		parent_id = category.get_attr(category_id, category.parent_id)
		if not parent_id or parent_id == 0:
			return category_id
		category_id = parent_id


if __name__ == '__main__':
	analysis()
