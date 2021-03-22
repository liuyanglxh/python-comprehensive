import csv
import json

import requests

dm_file_path = "/Users/liuyang/Downloads/dm.csv"
ls_file_path = "/Users/liuyang/Downloads/ls.sephora.com.20200621.20200623.csv"
target_file_path = "/Users/liuyang/Downloads/extra.csv"

dm_ids, dm_ids_list, extra_rows, extra_ids = set(), [], [], []
with open(dm_file_path) as dm_file:
	csv_reader = csv.reader(dm_file)
	header = next(csv_reader)
	for row in csv_reader:
		dm_ids.add(row[2])
		dm_ids_list.append(row[2])

with open(ls_file_path) as ls_file:
	csv_reader = csv.reader(ls_file)
	head = next(csv_reader)
	for row in csv_reader:
		line = row[0]
		if len(line) == 0 or not line.__contains__("_"): continue
		if not dm_ids.__contains__(line.split("_")[0]):
			extra_rows.append(row)
			extra_ids.append(line.split("_")[0])

titles = ["clickId", "time", "id", "type", "itemId", "spId",
		  "deviceType", "platform", "rip", "rip_position", "rip_value", "position"]

url = "https://ws.dealmoon.com/rank-server/api/surpport/v1/dealClickInfo"
dm_info_path = "/Users/liuyang/Downloads/dm_info.csv"
extra_info_path = "/Users/liuyang/Downloads/extra_info.csv"

headers = {"Content-Type": "application/json"}
# 已有的ids
step = 10

def abc(pa, id_list):
	with open(pa, "w", newline='') as target:
		writer = csv.DictWriter(target, fieldnames=titles)
		writer.writeheader()
		for i in range(0, len(id_list), step):
			try:
				ids = id_list[i:i + step]
				data = {"clickIds": ids, "years": [2020]}
				response = requests.post(url=url, data=json.dumps(data), headers=headers)
				js = response.json()
				dataList = js.get("dataList")
				if not dataList: continue
				for x in dataList:
					print(x)
					row = {}
					for h in titles:
						row[h] = x.get(h)
					writer.writerow(row)

			except Exception as e:
				print(e)
		target.close()


path, ids = dm_info_path, dm_ids_list
abc(path, ids)
path, ids = extra_info_path, extra_ids
abc(path, ids)
