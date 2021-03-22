import json
from util import mysql_local, file_util

if __name__ == '__main__':
	sql = 'select udid, name from eval_user_base_info'
	data = []
	for x in mysql_local.execute_sql(sql, 'recdb'):
		udid, name = x
		info = {'udid': udid, 'name': name}
		data.append(json.dumps(info))
	file_util.append_lines('/tmp/eval_user.txt', data)
