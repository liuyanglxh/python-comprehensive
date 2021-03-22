import time
from threading import RLock

from boltons.cacheutils import LRU

'''
1.没有批量方法
2.没有过期时间
https://boltons.readthedocs.io/en/latest/cacheutils.html#least-recently-used-lru
'''


class CacheModule:
	def __init__(self, max_size: int, ttl_millis: int, from_remote):
		'''
		:param max_size: max_size of the cache,using LRU
		:param ttl_millis: max live time for the objects
		:param from_remote: function to load data if the key not exists
		'''
		self.cache = LRU(max_size=max_size)
		self.ttl = ttl_millis
		self.from_remote = from_remote
		self._lock = RLock()

	def multi_get(self, keys) -> dict:
		result, missing = {}, []

		now = int(round(time.time() * 1000))
		for key in keys:
			value: dict = self.cache.get(key)
			# key未命中
			if not value:
				missing.append(key)
			# key超时
			elif now < value['max_time']:
				missing.append(key)
			# key存在且不是默认值
			elif value['data']:
				result[key] = value['data']

		if len(missing) > 0:
			loads_d: dict = self.from_remote(missing)
			dft = {'max_time': int(round(time.time() * 1000)) + self.ttl, 'data': {}}
			for key in missing:
				loads_d.setdefault(key, dft)
			self.multi_set(loads_d)
		return result

	def multi_set(self, data: dict):
		with self._lock:
			for k, v in data.items():
				self.cache.setdefault(k, v)

	def remove(self, keys):
		with self._lock:
			for key in keys:
				self.cache.pop(key)


if __name__ == '__main__':
	pass
