import json

d = {}
err = {}
with open("click.1614240003437.log.tmp") as f:
	while True:
		l = f.readline()

		if not l: break
		j = json.loads(l)
		value = j.get('value')
		platform = value.get('platform')

		data = value.get('data')
		res_type = data.get('res_type') if data.get('res_type') else "None"
		ad_type = data.get("ad_type") if data.get("ad_type") else "None"

		info = res_type + " " + ad_type
		d.setdefault(platform, set())
		d.get(platform).add(info)

		if res_type == 'None' and ad_type == 'None':
			page, module = value.get('page') if value.get('page') else "None", value.get('module') if value.get('module') else "None"
			asdfas = page+" "+module
			if not err.__contains__(asdfas):
				err[asdfas]=j

for k in d.keys():
	d[k] = list(d.get(k))

print(json.dumps(d))
print(json.dumps(err))
