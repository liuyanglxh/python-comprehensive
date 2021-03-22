import json
import sys

sp = "<.>"


def recursive(info, total, path):
	'''
	:param info: 当前info
	:param total: 总的info
	:param path: 路径
	:return:
	'''
	name, cost = info.get('name'), info.get('cost')
	if not path:
		path = name
	else:
		path = path + sp + name
	total.setdefault(path, {
		'times': 0,
		'cost': 0
	})
	this_info = total.get(path)
	this_info['times'] += 1
	this_info['cost'] += cost
	if info.get('sub'):
		for s in info.get('sub'):
			recursive(s, total, path)


def cal_avg(info: dict):
	for k, v in info.items():
		v['avg'] = str(round(v['cost'] / v['times'], 2)) + " ms"


def struct(info: dict) -> dict:
	result = {}
	for k, v in info.items():
		cur, n = result, k
		splt = k.split(sp)
		for i in range(0, len(splt) - 1):
			name = splt[i]
			n = name
			cur.setdefault('name', name)
			cur.setdefault('sub', [])
			ne = None
			sub = cur.get('sub')
			for s in sub:
				if s.get('name') and s.get('name') == splt[i + 1]:
					ne = s
					break
			if not ne:
				ne = {}
				sub.append(ne)
			cur = ne

		cur['name'] = splt[len(splt) - 1]
		cur['cost'] = v['cost']
		cur['avg'] = v['avg']
		cur['times'] = v['times']

	return result


def sort_field(d):
	return d['avg']


def sort(info):
	if info.get('sub'):
		l: list = info.get('sub')
		l.sort(key=sort_field, reverse=True)
		for x in l:
			sort(x)


if __name__ == '__main__':
	path = sys.argv[1]

	total = {}

	with open(path) as f:
		while True:
			line = f.readline()
			if not line: break
			try:
				j = json.loads(line)
			except:
				continue
			if j.get('mark') and j.get('mark') != 'time_marker':
				print('not ok')
				continue
			print('ok')
			recursive(j, total, None)
	print('done start analysis')

	print(json.dumps(total))
	cal_avg(total)
	print(total)
	total = struct(total)
	print(total)
	sort(total)
	print(total)
