import requests

url='https://ws.it4.dealmoon.net/recommend-engine/api/recommend-engine/extract-tag/tokenize'
headers={"Content-Type":"application/json"}
params={"text":"8倍视黄醇面部精华30ml;保湿精华30ml+眼部精华30ml;基础旅行套装;3号紧致晚霜50ml;1号卸妆水200ml;4号抗氧化保湿锁水精华液30ml;亮白淡斑精华15ml;10号手部精华30ml;5号抗老眼部精华30ml"}
response = requests.post(url=url, json=params, headers=headers)

print(response.json())