import json, os

if __name__ == '__main__':
	dir = '/tmp/ly'
	s = set()
	for filename in os.listdir(dir):
		if not filename.endswith('.log'): continue
		all_path = dir + "/" + filename
		with open(all_path) as f:
			while True:
				line = f.readline()
				if not line:
					break
				d = json.loads(line)
				if 'class' not in d or d['class'] != 'biz.hot_deal': continue

				if 'value' not in d: continue
				value = d['value']
				if 'dealId' not in value: continue
				if value.get('type') != 'deal': continue
				dealId = value['dealId']
				id = value.get('id')
				# if dealId == '0' or dealId == 0:
				if not id:
					fields = ['platform', 'clickPage', 'dealId', 'type', 'itemId', 'rip', 'rip_value']
					# print(json.dumps([value.get(field) for field in fields], ensure_ascii=False))
					# print(json.dumps(d))
					s.add(value.get('ua'))

	print(json.dumps([x for x in s]))

