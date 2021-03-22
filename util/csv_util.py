import csv
from util.file_util import __check_and_create_file


def append_head(file_path: str, data: list):
	"""
	写入标题
	:param file_path:
	:param data:
	:return:
	"""
	__check_and_create_file(file_path)
	with open(file_path, "w", newline='') as target:
		writer = csv.writer(target)
		writer.writerow(data)
		target.close()


def append_line(file_path: str, data: list):
	"""
	追加单行
	:param file_path:
	:param data:
	:return:
	"""
	__check_and_create_file(file_path)
	with open(file_path, 'a+') as target:
		writer = csv.writer(target)
		writer.writerow(data)
		target.close()


def append_lines(file_path: str, data: list):
	"""
	追加多行
	:param file_path:
	:param data:
	:return:
	"""
	__check_and_create_file(file_path)
	with open(file_path, "a+") as target:
		writer = csv.writer(target)
		for lst in data:
			writer.writerow(lst)
		target.close()


def cover(file_path: str, heads: list, data_dict: list):
	"""
	覆盖原来的数据，写入新的数据
	:param file_path:
	:param heads:	标题
	:param data_dict:	数据
	[
		{
			标题1:值,
			标题2:值,
			标题3:值,
		},
		...
	]
	:return:
	"""
	__check_and_create_file(file_path)
	with open(file_path, 'w') as target:
		writer = csv.writer(target)
		writer.writerow(heads)
		for d in data_dict:
			lst = []
			for head in heads:
				lst.append(d.get(head) if head in d else "")
			writer.writerow(lst)
		target.close()


if __name__ == '__main__':
	pass
