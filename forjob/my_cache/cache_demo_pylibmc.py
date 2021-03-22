import time

from cacheout import *

'''
https://cacheout.readthedocs.io/en/latest/
优：有批量方法；提供LRU算法，并有maxSize和ttl；
劣：multi_get方法是加锁的
'''
cache = LRUCache(maxsize=2, ttl=2)
fIFOCache = FIFOCache(maxsize=2, ttl=60)

ch = LFUCache()


class CacheModule(LRUCache):
	def __init__(self, maxsize, ttl, on_missing):
		'''
		:param maxsize:	max size of the cache
		:param ttl:	time to live for the objects
		:param on_missing: a function that returns a dict when keys are missing from the cache
		'''
		super().__init__(maxsize=maxsize, ttl=ttl)
		self.on_missing = on_missing

	def get_many(self, iteratee, default=None):
		d: dict = super().get_many(iteratee, default)
		result = {}
		for k, v in d.items():
			if v is not None:
				result[k] = v

		missing = [key for key in iteratee if key not in d or not d.get(key)]
		if len(missing) > 0:
			missing_d: dict = self.on_missing(missing)
			for k, v in missing_d.items():
				result[k] = v
			dft = {}
			for missing_key in missing:
				missing_d.setdefault(missing_key, dft)
			self.set_many(missing_d)

		return result


def get_from_remote(ids):
	print("from remote", ids)
	rslt = {}
	for i in ids:
		if i == 10: continue
		rslt[i] = str(i + 1)
	return rslt


if __name__ == '__main__':
	ch = CacheModule(maxsize=10, ttl=2, on_missing=get_from_remote)
	d = ch.get_many([1, 2, 3, 10])
	print(d)
	time.sleep(3)
	d = ch.get_many([1, 2, 3, 10])
	print(d)
