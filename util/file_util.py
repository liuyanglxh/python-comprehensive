import os


def read_file(path: str, handle_line):
	"""
	读取文件内容
	:param	处理line的函数
	"""
	with open(path, 'r') as f:
		while True:
			line = f.readline()
			if not line: break
			if handle_line(line) == 'break':
				break


def append_lines(path: str, data: list):
	"""
	追加行到文件
	:param path:
	:param data:
	:return:
	"""
	__check_and_create_file(path)
	with open(path, 'a') as f:
		for d in data:
			f.write(str(d) + "\n")


def cover(path: str, data: list):
	"""
	覆盖文件
	:param path:
	:param data:
	:return:
	"""
	__check_and_create_file(path)
	with open(path, 'w') as f:
		for x in data: f.write(str(x) + "\n")


def __check_and_create_file(path: str):
	"""
	文件如果不存在就创建
	:param path:
	:return:
	"""
	if not path.startswith("/"): raise Exception("文件需要完整路径")

	if os.path.exists(path): return

	for dir in __get_dirs__(path):
		if not os.path.exists(dir): os.mkdir(dir)

	file = open(path, 'w')
	file.close()


def __get_dirs__(path: str) -> list:
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
