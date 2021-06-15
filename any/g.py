old = """,au_ugc_fixed_post_p,au_ugc_guide_c,au_ugc_guide_u,au_ugc_post_c,au_ugc_post_u,au_ugc_topic_c,
au_ugc_topic_u,au_user_deal_click_info_2018,au_user_deal_click_info_2019,au_user_deal_click_info_2020,
au_user_deal_click_info_2021,ca_ugc_fixed_post_p,ca_ugc_guide_c,ca_ugc_guide_u,ca_ugc_post_c,ca_ugc_post_u,
ca_ugc_topic_c,ca_ugc_topic_u,ca_user_deal_click_info_2018,ca_user_deal_click_info_2019,ca_user_deal_click_info_2020,
ca_user_deal_click_info_2021,ca_user_deal_click_info_test_2019,de_ugc_guide_c,de_ugc_guide_u,
de_user_deal_click_info_2019,de_user_deal_click_info_2020,de_user_deal_click_info_2021,deal_click_info_2018,
deal_click_info_2019,deal_click_info_2020,deal_click_info_2021,deal_click_info_2022,deal_click_info_test_2019,
fr_ugc_fixed_post_p,fr_ugc_guide_c,fr_ugc_guide_u,fr_ugc_post_c,fr_ugc_post_u,fr_ugc_topic_c,
fr_user_deal_click_info_2019,fr_user_deal_click_info_2020,fr_user_deal_click_info_2021,kafka_topic_offset_org,
kol_candidate,ugc__c,ugc__u,ugc_fixed_post_p,ugc_guide_c,ugc_guide_c_v2,ugc_guide_u,ugc_guide_u_v2,ugc_local-deal_c,
ugc_local-deal_u,ugc_post_c,ugc_post_u,ugc_topic_c,ugc_topic_u,uk_ugc__c,uk_ugc__u,uk_ugc_fixed_post_p,
uk_ugc_guide_c,uk_ugc_guide_u,uk_ugc_post_c,uk_ugc_post_u,uk_ugc_topic_c,uk_ugc_topic_u,uk_user_deal_click_info_2018,
uk_user_deal_click_info_2019,uk_user_deal_click_info_2020,uk_user_deal_click_info_2021,user_deal_click_info_2018,
user_deal_click_info_2019,user_deal_click_info_2020,user_deal_click_info_2021,user_deal_click_info_2022,
user_deal_click_info_test_2019"""
new = """au_user_deal_click_info_2018,au_user_deal_click_info_2019,au_user_deal_click_info_2020,
ca_user_deal_click_info_2018,ca_user_deal_click_info_2019,ca_user_deal_click_info_2020,de_user_deal_click_info_2019,
de_user_deal_click_info_2020,deal_click_info_2018,deal_click_info_2020,deal_click_info_2021,
fr_user_deal_click_info_2019,fr_user_deal_click_info_2020,ugc_deal_c,ugc_deal_u,ugc_guide_c,ugc_guide_u,ugc_post_c,
ugc_post_u,uk_user_deal_click_info_2018,uk_user_deal_click_info_2019,uk_user_deal_click_info_2020,
user_deal_click_info_2018,user_deal_click_info_2019,user_deal_click_info_2020,user_deal_click_info_2021"""
plan_to_go = """
22.8 M   68.3 M   /apps/hbase/data/data/default/APP_CLICK
516.8 M  1.5 G    /apps/hbase/data/data/default/APP_IMPRESSION
46.2 K   138.6 K  /apps/hbase/data/data/default/CONTENT_DATA
17.2 M   51.5 M   /apps/hbase/data/data/default/OPERATION_REC_BUY
52.9 M   158.6 M  /apps/hbase/data/data/default/OPERATION_REC_CLICK
19.7 M   59.1 M   /apps/hbase/data/data/default/OPERATION_REC_DEAL_STATS
1.1 G    3.4 G    /apps/hbase/data/data/default/OPERATION_REC_IMPRESSION
50.2 K   150.7 K  /apps/hbase/data/data/default/SYSTEM.CATALOG
1.2 K    3.7 K    /apps/hbase/data/data/default/SYSTEM.FUNCTION
2.7 K    8.1 K    /apps/hbase/data/data/default/SYSTEM.LOG
4.9 K    14.6 K   /apps/hbase/data/data/default/SYSTEM.MUTEX
6.0 K    18.0 K   /apps/hbase/data/data/default/SYSTEM.SEQUENCE
12.9 K   38.7 K   /apps/hbase/data/data/default/SYSTEM.STATS
938.9 M  2.8 G    /apps/hbase/data/data/default/USER_BADGE_RECORD
30.3 M   90.8 M   /apps/hbase/data/data/default/USER_CLICK_RECORD
257.0 M  770.9 M  /apps/hbase/data/data/default/USER_IMPRESSION_RECORD
207.6 M  622.9 M  /apps/hbase/data/data/default/USER_IMPRESSION_RECORD_CATEGORY_NEW
1.9 M    5.8 M    /apps/hbase/data/data/default/au_ugc_fixed_post_p
19.4 M   58.3 M   /apps/hbase/data/data/default/au_ugc_guide_c
6.5 M    19.5 M   /apps/hbase/data/data/default/au_ugc_guide_u
39.7 M   119.1 M  /apps/hbase/data/data/default/au_ugc_post_c
14.0 M   42.1 M   /apps/hbase/data/data/default/au_ugc_post_u
6.2 K    18.6 K   /apps/hbase/data/data/default/au_ugc_topic_c
5.7 K    17.0 K   /apps/hbase/data/data/default/au_ugc_topic_u



276.2 K  828.7 K  /apps/hbase/data/data/default/au_user_deal_click_info_2021
9.0 M    27.1 M   /apps/hbase/data/data/default/ca_ugc_fixed_post_p
62.5 M   187.6 M  /apps/hbase/data/data/default/ca_ugc_guide_c
24.4 M   73.3 M   /apps/hbase/data/data/default/ca_ugc_guide_u
256.2 M  768.6 M  /apps/hbase/data/data/default/ca_ugc_post_c
99.0 M   296.9 M  /apps/hbase/data/data/default/ca_ugc_post_u
7.1 K    21.3 K   /apps/hbase/data/data/default/ca_ugc_topic_c
6.4 K    19.3 K   /apps/hbase/data/data/default/ca_ugc_topic_u


838.3 K  2.5 M    /apps/hbase/data/data/default/ca_user_deal_click_info_2021		
6.4 K    19.2 K   /apps/hbase/data/data/default/ca_user_deal_click_info_test_2019	xxxxxxx
44.4 K   133.1 K  /apps/hbase/data/data/default/de_ugc_guide_c
18.2 K   54.6 K   /apps/hbase/data/data/default/de_ugc_guide_u

143.3 K  430.0 K  /apps/hbase/data/data/default/de_user_deal_click_info_2021

331.8 G  995.3 G  /apps/hbase/data/data/default/deal_click_info_2019	xxxxxxxxxx
	
108.5 G  325.6 G  /apps/hbase/data/data/default/deal_click_info_2021    1621237614(快照)      
543      1.6 K    /apps/hbase/data/data/default/deal_click_info_2022

148.0 K  444.1 K  /apps/hbase/data/data/default/fr_ugc_fixed_post_p
5.3 M    15.8 M   /apps/hbase/data/data/default/fr_ugc_guide_c
1.9 M    5.6 M    /apps/hbase/data/data/default/fr_ugc_guide_u
1.7 M    5.2 M    /apps/hbase/data/data/default/fr_ugc_post_c
664.0 K  1.9 M    /apps/hbase/data/data/default/fr_ugc_post_u
5.5 K    16.5 K   /apps/hbase/data/data/default/fr_ugc_topic_c

37.8 K   113.5 K  /apps/hbase/data/data/default/fr_user_deal_click_info_2021
44.6 K   133.7 K  /apps/hbase/data/data/default/ugc__c
22.6 K   67.9 K   /apps/hbase/data/data/default/ugc__u
704.7 M  2.1 G    /apps/hbase/data/data/default/ugc_fixed_post_p
4.6 G    13.8 G   /apps/hbase/data/data/default/ugc_guide_c         1621238610(快照时间）     
531      1.6 K    /apps/hbase/data/data/default/ugc_guide_c_v2
2.3 G    6.8 G    /apps/hbase/data/data/default/ugc_guide_u         1621238640（快照时间）
10.3 K   30.8 K   /apps/hbase/data/data/default/ugc_guide_u_v2
7.1 K    21.3 K   /apps/hbase/data/data/default/ugc_local-deal_c
5.9 K    17.8 K   /apps/hbase/data/data/default/ugc_local-deal_u
54.5 G   163.5 G  /apps/hbase/data/data/default/ugc_post_c          1621238676（快照时间）
26.0 G   78.1 G   /apps/hbase/data/data/default/ugc_post_u          1621245443（快照时间）
20.3 K   61.0 K   /apps/hbase/data/data/default/ugc_topic_c
15.3 K   45.9 K   /apps/hbase/data/data/default/ugc_topic_u
6.4 K    19.3 K   /apps/hbase/data/data/default/uk_ugc__c
5.6 K    16.8 K   /apps/hbase/data/data/default/uk_ugc__u
6.9 M    20.7 M   /apps/hbase/data/data/default/uk_ugc_fixed_post_p
55.6 M   166.7 M  /apps/hbase/data/data/default/uk_ugc_guide_c
24.2 M   72.6 M   /apps/hbase/data/data/default/uk_ugc_guide_u
149.9 M  449.8 M  /apps/hbase/data/data/default/uk_ugc_post_c
67.5 M   202.4 M  /apps/hbase/data/data/default/uk_ugc_post_u
6.0 K    18.1 K   /apps/hbase/data/data/default/uk_ugc_topic_c
5.5 K    16.4 K   /apps/hbase/data/data/default/uk_ugc_topic_u
651.9 K  1.9 M    /apps/hbase/data/data/default/uk_user_deal_click_info_2021
10.7 M   32.2 M   /apps/hbase/data/data/default/user_deal_click_info_2021
553      1.6 K    /apps/hbase/data/data/default/user_deal_click_info_2022
"""

old = [x.strip() for x in old.split(',')]
new = {x.strip() for x in new.split(',')}
to_go = {x for x in old if x not in new}
print(to_go)
print('-----')
for x in plan_to_go.split('\n'):
	tb = x.strip().split('/')[-1].split(' ')[0]
	if tb not in to_go:
		print(tb)
