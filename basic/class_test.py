import sys


class Human:
	def __init__(self, name: str):
		self.name = name

	def change_namge(self, name: str):
		self.name = name


def er():
	a = 1 / 0


def a():
	er()


if __name__ == '__main__':

	try:
		a()
	except Exception as e:
		info = sys.exc_info()
		for x in info:
			print(x.tb_frame.f_back)
