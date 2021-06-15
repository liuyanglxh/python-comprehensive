# 全量的表
small_tables = """
17.2 M   51.5 M   /apps/hbase/data/data/default/OPERATION_REC_BUY
19.7 M   59.1 M   /apps/hbase/data/data/default/OPERATION_REC_DEAL_STATS
30.3 M   90.8 M   /apps/hbase/data/data/default/USER_CLICK_RECORD
1.9 M    5.8 M    /apps/hbase/data/data/default/au_ugc_fixed_post_p
19.4 M   58.3 M   /apps/hbase/data/data/default/au_ugc_guide_c
14.0 M   42.1 M   /apps/hbase/data/data/default/au_ugc_post_u
6.2 K    18.6 K   /apps/hbase/data/data/default/au_ugc_topic_c
5.7 K    17.0 K   /apps/hbase/data/data/default/au_ugc_topic_u
9.0 M    27.1 M   /apps/hbase/data/data/default/ca_ugc_fixed_post_p
24.4 M   73.3 M   /apps/hbase/data/data/default/ca_ugc_guide_u
7.1 K    21.3 K   /apps/hbase/data/data/default/ca_ugc_topic_c
6.4 K    19.3 K   /apps/hbase/data/data/default/ca_ugc_topic_u
838.3 K  2.5 M    /apps/hbase/data/data/default/ca_user_deal_click_info_2021		
44.4 K   133.1 K  /apps/hbase/data/data/default/de_ugc_guide_c
18.2 K   54.6 K   /apps/hbase/data/data/default/de_ugc_guide_u
143.3 K  430.0 K  /apps/hbase/data/data/default/de_user_deal_click_info_2021
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
531      1.6 K    /apps/hbase/data/data/default/ugc_guide_c_v2
10.3 K   30.8 K   /apps/hbase/data/data/default/ugc_guide_u_v2
7.1 K    21.3 K   /apps/hbase/data/data/default/ugc_local-deal_c
5.9 K    17.8 K   /apps/hbase/data/data/default/ugc_local-deal_u
20.3 K   61.0 K   /apps/hbase/data/data/default/ugc_topic_c
15.3 K   45.9 K   /apps/hbase/data/data/default/ugc_topic_u
6.4 K    19.3 K   /apps/hbase/data/data/default/uk_ugc__c
5.6 K    16.8 K   /apps/hbase/data/data/default/uk_ugc__u
6.9 M    20.7 M   /apps/hbase/data/data/default/uk_ugc_fixed_post_p
24.2 M   72.6 M   /apps/hbase/data/data/default/uk_ugc_guide_u
6.0 K    18.1 K   /apps/hbase/data/data/default/uk_ugc_topic_c
5.5 K    16.4 K   /apps/hbase/data/data/default/uk_ugc_topic_u
651.9 K  1.9 M    /apps/hbase/data/data/default/uk_user_deal_click_info_2021
10.7 M   32.2 M   /apps/hbase/data/data/default/user_deal_click_info_2021
553      1.6 K    /apps/hbase/data/data/default/user_deal_click_info_2022
"""
# 全量的表
big_tables = """
516.8 M  1.5 G    /apps/hbase/data/data/default/APP_IMPRESSION
52.9 M   158.6 M  /apps/hbase/data/data/default/OPERATION_REC_CLICK
1.1 G    3.4 G    /apps/hbase/data/data/default/OPERATION_REC_IMPRESSION
938.9 M  2.8 G    /apps/hbase/data/data/default/USER_BADGE_RECORD
257.0 M  770.9 M  /apps/hbase/data/data/default/USER_IMPRESSION_RECORD
207.6 M  622.9 M  /apps/hbase/data/data/default/USER_IMPRESSION_RECORD_CATEGORY_NEW
39.7 M   119.1 M  /apps/hbase/data/data/default/au_ugc_post_c
276.2 K  828.7 K  /apps/hbase/data/data/default/au_user_deal_click_info_2021
62.5 M   187.6 M  /apps/hbase/data/data/default/ca_ugc_guide_c
256.2 M  768.6 M  /apps/hbase/data/data/default/ca_ugc_post_c
99.0 M   296.9 M  /apps/hbase/data/data/default/ca_ugc_post_u
704.7 M  2.1 G    /apps/hbase/data/data/default/ugc_fixed_post_p
55.6 M   166.7 M  /apps/hbase/data/data/default/uk_ugc_guide_c
149.9 M  449.8 M  /apps/hbase/data/data/default/uk_ugc_post_c
67.5 M   202.4 M  /apps/hbase/data/data/default/uk_ugc_post_u
"""
# 增量的表
incrs = """
6.5 M    19.5 M   /apps/hbase/data/data/default/au_ugc_guide_u      1621579542383(时间)，当前总数128078；
4.6 G    13.8 G   /apps/hbase/data/data/default/ugc_guide_c         1621238610(快照时间）     
108.5 G  325.6 G  /apps/hbase/data/data/default/deal_click_info_2021    1621237614(快照)   
2.3 G    6.8 G    /apps/hbase/data/data/default/ugc_guide_u         1621238640（快照时间）    @5.21 15:11 总数43417023行
54.5 G   163.5 G  /apps/hbase/data/data/default/ugc_post_c          1621238676（快照时间）
26.0 G   78.1 G   /apps/hbase/data/data/default/ugc_post_u          1621245443（快照时间）
"""
