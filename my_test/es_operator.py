from util import elasticsearch_util

data = [
	{"first": "will", "last": "smith"},
	{"first": "smith", "last": "jones"},
	{"first": "smith", "last": "lily"},
	{"first": "smith", "last": "jackson"},
	{"first": "lulu", "last": "jones"},
	{"first": "will", "last": "jones"},
]

if __name__ == "__main__":
	for index in range(0, len(data)):
		elasticsearch_util.insert("cross_demo", "doc", index, data[index])
