s = '''
| 2021-02-01     | 4651    | 35.7  |
| 2021-02-02     | 4057    | 36.3  |
| 2021-02-03     | 4159    | 38.2  |
| 2021-02-04     | 4520    | 36.6  |
| 2021-02-05     | 4372    | 31.0  |
| 2021-02-06     | 4295    | 32.9  |
| 2021-02-07     | 4176    | 31.8  |
'''

splt = s.split("\n")
for x in splt:
	x = x.replace(" ", "")
	if x == '': continue
	x2 = x.split("|")
	day = "'" + x2[1] + "'"
	cnt = x2[2]
	print("select deal_nums from temp_rec_imp where create_day = ", day, "order by deal_nums desc limit",
		  int(int(cnt) * 0.99), ",1;")
	print("select deal_nums from temp_rec_imp where create_day = ", day, "order by deal_nums desc limit",
		  int(int(cnt) * 0.90), ",1;")
	print("select deal_nums from temp_rec_imp where create_day = ", day, "order by deal_nums desc limit",
		  int(int(cnt) * 0.75), ",1;")
	print("select deal_nums from temp_rec_imp where create_day = ", day, "order by deal_nums desc limit",
		  int(int(cnt) * 0.50), ",1;")
	print("select deal_nums from temp_rec_imp where create_day = ", day, "order by deal_nums desc limit",
		  int(int(cnt) * 0.25), ",1;")
	print("---------")
