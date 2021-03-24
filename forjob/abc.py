import json

from util import file_util, my_json

if __name__ == '__main__':
	dir = '/tmp/ly/ly'
	dest = '/tmp/ly/0dealId.txt'
	lst = []


	def func(line):
		info = json.loads(line)
		if 'value' not in info: return
		value = info['value']
		if 'dealId' not in value: return
		dealId = value['dealId']
		if dealId == '0' or dealId == 0:
			lst.append(info)

		return 'break'


	file_util.read_dir(dir, func)

	lst2 = []
	for x in lst:
		value = x['value']

		d = {
			'rip': value['rip'],
			'rip_value': value['rip_value'],
			'rip_position': value['rip_position'],
			'itemId': value['itemId'],
			'name': x['class'] + "." + x['name'],
			'clickId': value['clickId'],
			'platform': value['platform'],
		}
		if 'dm_data' in value: d['dm_data'] = json.loads(value['dm_data'])
		if 'clickPage' in value: d['clickPage'] = value['clickPage']

		lst2.append(d)
	# print(my_json.dumps(lst2))
	# print(my_json.dumps(lst))

