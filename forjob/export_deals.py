import pymysql, time, csv

db_host, db_user, db_pass = "s.dealmoon.db.dealmoon.net", "bigdata", "bookface06"

conn = pymysql.connect(db_host, db_user, db_pass, "recdb")

header = ["id", "中文标题", "商家名", "浏览数", "分享数", "点击数", "收藏数", "评论数", "发布时间", "初次发布时间"]

max_publish_time = 1613617453 - 90 * 24 * 60


def getFormatedTime(secs):
	if secs == 0: return "--"
	return time.strftime('%Y年%m月%d日%H时', time.localtime(int(secs)))


def do_write_to_csv(infos, filepath):
	with open(filepath, 'w', encoding='utf-8', newline='') as f:
		writer = csv.DictWriter(f, header)
		writer.writeheader()
		writer.writerows(infos)


# 查textTags为NOTAG的折扣id
def getNoTextTagsIds():
	deal_ids = []
	cur = conn.cursor()
	try:
		sql = "select distinct(docid) from recdb.recon_doc_tags_deal where text_tags = '[\"NOTAG\"]'"
		cur.execute(sql)
		for docid in cur.fetchall():
			deal_ids.append(docid[0])
		deal_ids.sort(reverse=True)
	finally:
		cur.close()
	return deal_ids


# 折扣库有但tag库没有的折扣id
def getNoTagsIds():
	deal_ids = []
	sql = '''
		SELECT distinct(di.id)
		FROM  dealmoon.deal_index di
		where di.dead_time > 1613617453 and en_state = 'published' and cn_state = 'published'
		and NOT EXISTS (
			SELECT id from recdb.recon_doc_tags_deal rdtd where di.id = rdtd .docid 
		);
	'''
	cur = conn.cursor()
	cur.execute(sql)
	try:
		for x in cur.fetchall():
			deal_ids.append(x[0])
	finally:
		cur.close()
	return deal_ids


def write_to_csv(ids, filepath):
	# 批量查询上限
	step = 100
	infos = []
	for index in range(0, len(ids), step):
		deal_ids = ids[index:index + step]
		if len(deal_ids) == 0:
			print("结束")
			break
		print("select ids from ", deal_ids[0], "to", deal_ids[len(deal_ids) - 1], filepath)

		sql = """
				SELECT di.id, dd.cn_title , dd.store_name , di.view_num , di.click_num, di.share_num ,di.favorite_num , di.comment_num , di.published_time,di.first_published_time 
				from dealmoon.deal_data dd 
				join dealmoon.deal_index di  on di.id = dd.deal_id 
				where dd.deal_id in  (%s)
			""" % ",".join(["%s"] * len(deal_ids))
		cur = conn.cursor()
		try:
			cur.execute(sql, deal_ids)
			for x in cur.fetchall():
				info = {'id': x[0],
						'中文标题': x[1],
						'商家名': x[2],
						'浏览数': x[3],
						'点击数': x[4],
						'分享数': x[5],
						'收藏数': x[6],
						'评论数': x[7],
						'发布时间': getFormatedTime(x[8]),
						'初次发布时间': getFormatedTime(x[9])}
				if int(x[8]) < max_publish_time: continue
				infos.append(info)
		finally:
			cur.close()
	do_write_to_csv(infos, filepath)


deal_ids1 = getNoTextTagsIds()
print("NOTAGS 个数", len(deal_ids1))
deal_ids2 = getNoTagsIds()
print("没有提取的个数", len(deal_ids2))

# 初始化文件
write_to_csv(deal_ids1, "/tmp/rec/no_text_tags.csv")
write_to_csv(deal_ids2, "/tmp/rec/no_tags.csv")

conn.close()


