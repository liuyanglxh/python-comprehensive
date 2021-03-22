import sys, json


def recursive(j, info: dict):
	info.setdefault(j.get('name'), {})
	d = info.get(j.get('name'))
	d.setdefault("cost", 0)
	d.setdefault("times", 0)
	d.setdefault('max', 0)
	d.setdefault('min', 9999999)
	this_cost = int(j.get('cost'))
	d['cost'] += this_cost
	d.setdefault('all', [])
	d['all'].append(this_cost)
	d['max'] = max(d['max'], this_cost)
	d['min'] = min(d['min'], this_cost)
	d['times'] += 1
	if j.get('sub'):
		for x in j.get('sub'):
			recursive(x, info)


def cal_avg(info: dict):
	for k, v in info.items():
		v['avg'] = str(round(int(v['cost']) / int(v['times']), 2)) + " ms"


def get_avg(d): return d['avg']


def handle_all(d: dict):
	if not d.get('all'): return
	l: list = d.get('all')
	l.sort()
	d['median_cost'] = str(l[int(len(l) / 2)]) + " ms"
	del d['all']


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
			recursive(j, total)
	for k, v in total.items():
		handle_all(v)
	print(json.dumps(total))
	cal_avg(total)
	print(json.dumps(total))
	lst = []
	for k, v in total.items():
		v['name'] = k
		lst.append(v)

	lst.sort(key=get_avg, reverse=True)
	print(json.dumps(lst))
