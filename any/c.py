from forjob.hive import beeline

sql_format1 = """
select log.`time`,log.id,log.udid
    from ods.ods_deal_index deal
    join ods.ods_impression_log log on log.id = deal.id
    where log.`time` between deal.published_time and deal.published_time+172800
    and lower(device) in ('iphone','android')
    and log.type='deal' and log.from_page='home_list' and lower(log.category_value)='new'
    and (log.from_model='feed_list' or log.from_model is null)
    and deal.id = %s;
"""
file = '/tmp/ly/impression.csv'

sql_format = sql_format1
if __name__ == '__main__':
	deal_ids = [2357781, 2358446, 2356300, 2356925, 2357568, 2357380, 2358665, 2359363]
	# sql_list = [sql_format % str(deal_id) for deal_id in deal_ids]
	# for x in sql_list: print(beeline.append(x, file))
	deal_ids = [str(a) for a in deal_ids]
	print("select min(published_time),max(published_time) from ods_deal_index where id in (%s)" % ','.join(deal_ids))
