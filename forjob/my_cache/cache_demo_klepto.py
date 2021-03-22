
import klepto
from klepto import *
'''

https://klepto.readthedocs.io/en/latest/klepto.html
'''

ch = klepto.lru_cache(maxsize=2, )

if __name__ == '__main__':
	a = ch.__get__(1)
	print(a)