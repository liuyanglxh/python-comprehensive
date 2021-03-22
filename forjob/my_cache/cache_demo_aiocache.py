from aiocache import SimpleMemoryCache

'''
https://aiocache.readthedocs.io/en/latest/
pip install aiocache
pip install aiocache[memcached]
'''

ch = SimpleMemoryCache()

if __name__ == '__main__':
	ch.multi_set([[1, {1: "1"}], [2, {2: "2"}]])
	d = ch.multi_get([1, 2, 3])
	print(d)
