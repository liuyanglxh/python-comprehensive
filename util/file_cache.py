class FileCache:
	def __init__(self, file: str, on_miss):
		self.file = file
		self.on_miss = on_miss

	def init(self, file):
		pass

	def get(self, keys: list) -> dict:
		pass
