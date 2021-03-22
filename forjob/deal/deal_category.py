import json

from util import file_util, mysql_local, my_json

local_file = '/tmp/category.txt'

cache = {}

"""
折扣分类缓存
"""


def init():
	"""
	初始化缓存
	"""
	global cache

	def func(line):
		row = json.loads(line)
		cache[int(row['id'])] = row

	file_util.read_file(local_file, func)

	print("初始化分类信息", len(cache))


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


def get(category_id: int):
	if not cache: init()
	return cache.get(category_id)


def get_attr(category_id: int, attr: str):
	if not cache: init()
	return cache.get(category_id).get(attr) if category_id in cache else ""


if __name__ == '__main__':
	print(get_attr(1175715921, 'label_en'))