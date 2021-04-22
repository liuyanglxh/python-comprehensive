from elasticsearch import Elasticsearch
import time

host = '127.0.0.1'
port = '9200'

es = Elasticsearch(host=host, port=port)


def insert(index: str, type: str, id: int, body: dict):
	es.index(index=index, doc_type=type, id=id, body=body, routing='1')


if __name__ == '__main__':
	data = [
		{
			'id': 1, 'title': '成都房价平稳', 'time': '2020-1-10',
			'desc': '涨幅越来越低', 'likes': 10
		},
		{
			'id': 2, 'title': '成都小吃', 'time': '2021-1-10',
			'desc': '成都小吃介绍', 'likes': 30
		},
		{
			'id': 3, 'title': '四川美食', 'time': '2019-1-10',
			'desc': '四川美食探店', 'likes': 5
		},
		{
			'id': 4, 'title': '成都运动', 'time': '2020-3-20',
			'desc': '成都马拉松', 'likes': 20
		},
		{
			'id': 5, 'title': '成都找工作', 'time': '2021-2-20',
			'desc': '成都软件园招聘', 'likes': 18
		},
		{
			'id': 6, 'title': '篮球公园', 'time': '2010-10-23',
			'desc': '勾手老大爷', 'likes': 9
		},

	]
	for body in data:
		id = body['id']
		del body['id']
		insert('search_demo', 'doc', id, body)
	print(int(time.time()))
