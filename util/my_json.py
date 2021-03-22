import json


def dumps(source):
	return json.dumps(source, ensure_ascii=False)
