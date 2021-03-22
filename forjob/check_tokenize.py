# 测试本地java分词和线上分词的效果对比

import requests
from urllib import parse


deal_ids: list = [2076611, 2076483, 2076538, 2076541, 2076450, 2076380, 2076281, 2076246, 2073484, 2069303, 2024185,
				  1990162, 2033514, 2076567, 2076559, 2073658, 2068419, 2042299, 2068419, 2076567]

info_url: str = "https://ws.dealmoon.com/deal/admin/deal/v1/cms/deal-basic-list"
tokenize_url: str = "http://ws.it4.dealmoon.net/recommend-service/admin/recommend/v1/test/test-tag-doc"
for deal_id in deal_ids:
	params: dict = {
		"dealIds": deal_id,
		"isAdState": False
	}
	headers: dict = {"Content-Type": "application/json"}
	real_url = "%s%s%s" % (info_url, "?", parse.urlencode(params))
	response = requests.get(url=real_url, headers=headers)
	data = response.json()
	if not data['data']: continue
	data = data['data'][0]
	tokenize_params: dict = {
		"type": "dealInfo",
		"dealInfos": [data]
	}
	print(tokenize_params)
	response = requests.post(url=tokenize_url, json=tokenize_params, headers=headers)
	print(response.json())
