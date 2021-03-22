with open('/tmp/deal_cate_lv1.txt') as f:
	while True:
		line = f.readline()
		if not line: break
		if line.__contains__('[') or line.__contains__(']') or line.__contains__(','):
			pass