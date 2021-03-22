from boltons.cacheutils import LRU


class CacheModule:

	def __init__(self, name, max_size=128, from_remote=None):
		'''
		:param max_size:	最大容量
		:param from_remote: 查询数据函数，返回值必须是一个dict
		:param ttl:	有效时间，单位：秒
		'''
		self.local_cache = LRU(max_size=max_size)
		self.from_remote = from_remote
		self.empty = {}
		self.name = name

	def get_all(self, keys: list) -> dict:
		result, missing_keys = {}, []

		for key in keys:
			val = self.local_cache.get(key)
			if val is not None:
				if val != self.empty:
					result[key] = val
			else:
				missing_keys.append(key)
		# 缓存未命中
		if len(missing_keys) > 0:
			missing_dict = self.reload(missing_keys)
			result = {**result, **missing_dict}

		return result

	def remove(self, keys: list):
		for key in keys: self.local_cache.__delitem__(key)

	def statistics(self):
		hitRateAsString = '%.3f' % (
				self.local_cache.hit_count / (self.local_cache.hit_count + self.local_cache.miss_count))
		return {
			"name": self.name,
			"hit_count": self.local_cache.hit_count,
			"miss_count": self.local_cache.miss_count,
			"size": len(self.local_cache.keys()),
			"hitRateAsString": hitRateAsString + "%",
		}

	def reload(self, keys: list) -> dict:
		d = {}
		missing_vals = self.from_remote(keys)
		# 不存在的值，设置为空
		if missing_vals:
			for key, val in missing_vals.items():
				self.local_cache.setdefault(key, val)
				d[key] = val
		for missing_key in keys: self.local_cache.setdefault(missing_key, self.empty)
		return d


def get_data(ids: list):
	print("get from remote ", ids)
	d = {}
	for id in ids: d[id] = str(id)
	return d


if __name__ == '__main__':
	ch = CacheModule("test", 200, from_remote=get_data)
	ch.get_all([1, 2, 3])
	ch.get_all([2, 3, 4])
	ch.get_all([2, 3, 4])
	ch.get_all([2, 3, 4])
	ch.remove([2, 3, 4])
	ch.get_all([2, 3, 4])
