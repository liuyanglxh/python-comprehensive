import pymysql
import random


def execute_sql(sql, db):
	db_host, db_user, db_pass = "s.dealmoon.db.dealmoon.net", "bigdata", "bookface06"
	conn = pymysql.connect(db_host, db_user, db_pass, db)
	cur = conn.cursor()
	try:
		cur.execute(sql)
		return cur.fetchall()
	finally:
		conn.close()


if __name__ == '__main__':
	pass
