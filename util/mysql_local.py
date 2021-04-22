import pymysql

"""
在电脑本地执行的sql工具
"""

recdb = 'recdb'
dealmoon = 'dealmoon'
ugc = 'ugc'


def execute_sql(sql, db):
	db_host, db_user, db_pass = "13.57.129.69", "cdoffice", "bookface06"
	conn = pymysql.connect(host=db_host, port=3306, user=db_user, passwd=db_pass, db=db)
	cur = conn.cursor()
	try:
		cur.execute(sql)
		return cur.fetchall()
	finally:
		conn.close()


if __name__ == '__main__':
	sql = "select * from deal_index where id = 254828;"
	for x in execute_sql(sql, 'dealmoon'):
		print(x)
