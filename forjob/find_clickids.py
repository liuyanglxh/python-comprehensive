import csv
import os

dm_file_path = "/Users/liuyang/Downloads/dm.csv"
ls_file_path = "/Users/liuyang/Downloads/ls.sephora.com.20200621.20200623.csv"
target_file_path = "/Users/liuyang/Downloads/extra.csv"

dm_ids, ls_rows = set(), []
with open(dm_file_path) as dm_file:
	csv_reader = csv.reader(dm_file)
	header = next(csv_reader)
	for row in csv_reader:
		dm_ids.add(row[2])

with open(ls_file_path) as ls_file:
	csv_reader = csv.reader(ls_file)
	head = next(csv_reader)
	for row in csv_reader:
		line = row[0]
		if len(line) == 0 or not line.__contains__("_"): continue
		if not dm_ids.__contains__(line.split("_")[0]):
			ls_rows.append(row)

with open(target_file_path, "w", newline='') as target:
	writer = csv.writer(target)
	writer.writerows([head])
	for x in ls_rows:
		writer.writerows([x])
	target.close()
