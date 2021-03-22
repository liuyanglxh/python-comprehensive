from cache.lru_cache import *

"""

"""
ch = LruCache(maxsize=200, timeout=60)




@LruCache(maxsize=20, timeout=10)
def get(id):
	print("id is " + id)
	return {"id": id}


if __name__ == '__main__':
	for x in range(0, 10):
		get(x)
