from util import elasticsearch_util

a1 = {
	'index': 'index1',
	'data': [
		{"first": "will", "last": "smith jackson lily"},  # 0
		{"first": "smith", "last": "jones"},  # 3
		{"first": "smith", "last": "lily"},  # 2
		{"first": "smith", "last": "jackson"},  # 4
		{"first": "lulu", "last": "jones"},  # 2
		{"first": "will", "last": "jones jones kelly"},  # 1
		{"first": "will", "last": "jones"},  # 1
	]
}

a2 = {
	'index': 'index2',
	'data2': [
		{'title': 'title1 is great and nice; i love title1; you have to read title1;title1;', 'comment': 10},
		{'title': 'title2 is bad', 'comment': 15},
		{'title': 'title3 is great', 'comment': 8},
		{'title': 'title1 is bad', 'comment': 12},
		{'title': 'title2 is great', 'comment': 13},
		{'title': 'title4 is great;i love title4!', 'comment': 8},
		{'title': 'title4 is great', 'comment': 9},
	]
}

data3 = [
	{'title': 'this is title1', 'time': '2021-03-01', 'use_decay': True},
	{'title': 'this is title2', 'time': '2020-01-11', 'use_decay': True},
	{'title': 'this is title3', 'time': '2021-02-23', 'use_decay': True},
	{'title': 'this is title4', 'time': '2020-10-07', 'use_decay': False},
	{'title': 'this is title5', 'time': '2021-01-01', 'use_decay': True},
]

data4 = [
	{'title': 'running man good man'},
	{'title': 'running girl bad'},
	{'title': 'running boy good'},
	{'title': 'walking man very good'},
	{'title': 'walking girl great and very nice'},
	{'title': 'walking boy awful'},
	{'title': 'sleeping man lazy and corrupt'},
]

data5 = {
	'index': 'script_fields',
	'data': [
		{'name': 'jackson', 'score': 12},
		{'name': 'lulu', 'score': 13},
		{'name': 'mack', 'score': 18},
	]
}


def do_index(name: str, d: list):
	for index, ele in enumerate(d):
		elasticsearch_util.insert(name, "doc", index, ele)


c = data5
if __name__ == "__main__":
	do_index(c['index'], c['data'])
