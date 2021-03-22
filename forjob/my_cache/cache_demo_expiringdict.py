from expiringdict import ExpiringDict

'''
https://pypi.org/project/expiringdict/
'''

ch = ExpiringDict(max_len=100, max_age_seconds=10)



ch.get(1)
ch.setdefault(1, {1:"1"})