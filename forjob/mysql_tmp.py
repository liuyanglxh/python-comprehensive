import pymysql


def execute_sql(sql):
	db_host, db_user, db_pass = "s.dealmoon.db.dealmoon.net", "bigdata", "bookface06"
	conn = pymysql.connect(db_host, db_user, db_pass, "recdb")
	cur = conn.cursor()
	try:
		cur.execute(sql)
		return cur.fetchall()
	finally:
		conn.close()


sql = """
	select id, if(en_state='hidden' and cn_state!='hidden', 1,0)
	from dealmoon.deal_index 
	where first_published_time between 1609488000 and  1612166399;
"""

data = execute_sql(sql)
cn_only_ids, other_ids = [], []
for d in data:
	if int(d[1]) == 1:
		cn_only_ids.append(int(d[0]))
	else:
		other_ids.append(int(d[0]))

local_file = '/tmp/bigdata/info_cn.txt'
with open(local_file, 'w') as f:
	for id in cn_only_ids:
		f.write(str(id)+"\t 1\n")
	# for id in other_ids:
	# 	f.write(str(id) + "\t 0\n")






