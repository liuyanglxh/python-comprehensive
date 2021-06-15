import requests
import re
import os
from urllib.request import urlretrieve


def get_url(key):
	url = 'https://xueshu.baidu.com/s?wd=' + key + '&&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_from=&sc_as_para=sc_lib%3A&rsv_sug2=0'
	return url


