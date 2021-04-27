def percent(numerator, denominator, round_num=2):
	return str(round(float(numerator * 100) / float(denominator), round_num)) + "%"


def divide(a, b, round_num=2):
	return round(float(a) / float(b), round_num)
