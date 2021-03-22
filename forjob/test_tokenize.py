# encoding:utf-8

import requests

url = 'http://10.0.20.37:9095/api/recommend-engine/extract-tag/tokenize'
url2 = 'https://ws.dealmoon.com/recommend-engine/api/recommend-engine/extract-tag/tokenize'
headers = {"Content-Type": "application/json"}

texts = "Asoph女装全场满50打八折满150打七折,BobbiBrown满75送正装唇釉,WOMENUPADDEDPARKA|UNIQLOUS棉袄白菜价,Clothing&AccessoriesClearance:Target女装热卖,Uniqlo季末折扣区男女服饰热卖,Chico's全场满百打五折,Bulova宝路华旗下Caravelle女士镶钻手镯式腕表,adidas男士长袖卫衣两件50刀折扣码DPFOIL,COACHOutlet配饰热卖复古爱心丝带$27，小飞象丝巾$29,Macy's精选被子三件套24.9刀一套,Sedona迷你方形和圆形铸铁锅两个,JabraElite75t真无线蓝牙耳机官翻,Americaneagle内裤5条15刀,Amazon.com|SamsoniteAspire万向轮硬壳行李箱两个,ImusaUSA14”轻质铸铁铁锅，不沾不锈钢把手,摩洛哥格子现代几何粉色地毯(2'0x3'0),DealoftheDay|KateSpadeSurprise,Amazon.com:JosephJosephCut&CarveMulti-FunctionCuttingBoard,Large,Red多功能砧板,OldNavy运动文胸10刀一件,SaleShopDesignerShoes-Women's|SaksFifthAvenue美鞋byfar"
for text in texts.split(","):
	params = {"text": text}
	response1 = requests.post(url=url, json=params, headers=headers)
	response2 = requests.post(url=url2, json=params, headers=headers)
	print(response1.json()["data"] == response2.json()["data"])
	if not response1.json()["data"] == response2.json()["data"]: print(text)
