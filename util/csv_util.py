import csv
import os


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


def __check_and_create_file(path: str):
	"""
	文件如果不存在就创建
	:param path:
	:return:
	"""
	if not path.startswith("/"): raise Exception("文件需要完整路径")

	if os.path.exists(path): return

	for dir in __get_dirs(path):
		if not os.path.exists(dir):
			os.mkdir(dir)

	file = open(path, 'w')
	file.close()


def __get_dirs(path: str) -> list:
	"""
	提取文件的文件夹，默认把最后一个/后面的当做文件名
	:param path:
	:return:
	"""
	splits = path.split("/")
	cur_dir, lst = '', []
	for index in range(0, len(splits) - 1):
		split = splits[index]
		if not split: continue
		cur_dir = cur_dir + "/" + split
		lst.append(cur_dir)
	return lst


if __name__ == '__main__':
	pass
