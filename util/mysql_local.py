import pymysql

"""
在电脑本地执行的sql工具
"""


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
	sql = 'select udid from eval_user_base_info'
	for x in execute_sql(sql, 'recdb'):
		print(x[0])
