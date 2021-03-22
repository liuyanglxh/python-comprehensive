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
	with open(path, 'a') as f:
		for d in data:
			f.write(str(d) + "\n")








