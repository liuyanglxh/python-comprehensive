def __cmd__(sql, file, mode) -> str:
	a = """
	    beeline -u "jdbc:hive2://master1:2181,master2:2181,slave1:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2" -nliuyang -pc2qGJ1GB --verbose=true  --showHeader=false --outputformat=csv2  --color=true  -e "set tez.grouping.split-count=1;set hive.exec.reducers.max=1;set tez.am.resource.memory.mb=1024;set hive.tez.container.size=1024;set tez.runtime.io.sort.mb=400;%s" %s %s
	""" % (sql.strip().replace("\n", " "), mode, file)
	return a.strip()


def append(sql, file) -> str:
	return __cmd__(sql, file, '>>')


def cover(sql, file) -> str:
	return __cmd__(sql, file, '>')


info2 = {
	"sql": """
	select distinct udid,strategy from ods.ods_impression_log
    where create_day between '2021-04-07' and '2021-04-20'
    and type='deal' and from_page='home_list' and scene = 'ad_list_new'
    and (ad_type is not null and length(ad_type)>0)
	""",
	"file": "/tmp/ly/abtest.csv"
}
info1 = {
	"sql": """
	select * from ods.ods_impression_log
    where create_day between '2021-04-19' and '2021-04-24' and lower(device) in ('iphone','android')
    and id in (2357781, 2358446, 2356300, 2356925, 2357568, 2357380, 2358665, 2359363)
    and type='deal' and from_page='home_list' and lower(category_value)='new'
    and (from_model='feed_list' or from_model is null);
	""",
	"file": "/tmp/ly/impression.csv"
}
info3 = {
	"sql": """
	select * from ods.ods_deal_event_log
    where create_day between '2021-04-19' and '2021-04-24' and rip='home_list'
    and type='deal' and op_type='click' and ad_type is null  and id is not null
    and id in (2357781, 2358446, 2356300, 2356925, 2357568, 2357380, 2358665, 2359363)
	""",
	"file": "/tmp/ly/click-1.csv"
}
info4 = {
	"sql": """
	select * from ods.ods_hot_deal_deal_ad_click_log
    where create_day  between '2021-04-19' and '2021-04-24' and rip='home_list'
    and type='deal' and op_type='click' and from_obj='ad' and ad_type is not null and length(ad_type)>0
    and category_value is not null and length(category_value)>0  and deal_id is not null
    and id in (2357781, 2358446, 2356300, 2356925, 2357568, 2357380, 2358665, 2359363)
	""",
	"file": "/tmp/ly/click-2.csv"
}
info5 = {
	"sql": """
	select * from ods.ods_hot_deal_deal_buy_log_modify
    where create_day between '2021-04-19' and '2021-04-24'
    and rip='home_list' and rip_position is not null and (ad_type is null or length(ad_type)=0)
    and (category_value is null or length(category_value)=0) and length(redirect_url)>0
    union
    select * from ods.ods_hot_deal_deal_buy_log_modify
    where create_day between '2021-04-19' and '2021-04-24'
    and rip='home_list_ad'  and (ad_type is not null and length(ad_type)>0)
    and (category_value is not null and length(category_value)>0) and length(redirect_url)>0
	""",
	"file": "/tmp/ly/deal-buy.csv"
}


def cover_(i):
	print(cover(i['sql'], i['file']))


info = info1
if __name__ == '__main__':
	# for x in [info3, info4, info5]:
	# 	info = x
	# 	print(cover(info['sql'], info['file']))
	cover_(info1)
