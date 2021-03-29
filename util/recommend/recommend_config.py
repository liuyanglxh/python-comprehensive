from util import mysql_local, my_json

db = 'recdb'


def get_by_name(name: str):
	sql = "select id,name,type,value,description,update_time from recommend_config where name = '%s'" % name
	lst = mysql_local.execute_sql(sql, db)
	if len(lst) == 0: return {}

	id, name, type, value, description, update_time = lst(sql, db)[0]
	return my_json.dumps(
		{
			'id': id,
			'name': name,
			'type': type,
			'value': value,
			'description': description,
			'update_time': update_time
		}
	)


def get_all():
	sql = 'select * from recommend_config'
	return mysql_local.execute_sql(sql, db)


if __name__ == '__main__':
	name = 'deal.rec.category.published.within.ms'
	print(get_by_name(name))
# print(my_json.dumps(get_all()))
