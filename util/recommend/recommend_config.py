from util import mysql_local


def get_by_name(name: str):
	sql = "select * from recommend_config where name = '%s'" % name
	return mysql_local.execute_sql(sql, 'recdb')


if __name__ == '__main__':
	name = 'deal.rec.category.published.within.ms'
	print(get_by_name(name))
