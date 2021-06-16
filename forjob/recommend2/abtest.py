"""
    ABtest：
    销量表：
    @dn1
    /home/opt/scripts/datasync/sqoop/shell
    sh -x order_history.sh order_history dw
    dm.dm_view_abtest_statistics	聚合表
    abtest表：
    @dn1
    /home/opt/scripts/datawarehouse/shell/abtest	2个脚本
    dwb.dwb_deal_abtest_statistics_detail	明细表
"""

hive_sql_detail = """
set tez.grouping.split-count=1;
set hive.exec.reducers.max=1;
set tez.am.resource.memory.mb=1024;
set hive.tez.container.size=1024;
set tez.runtime.io.sort.mb=400;
select t1.platform  , t1.category_value, t1.strategy, t1.click,t1.buy,t1.imp, t1.order_num, round(t1.click/t1.imp,6) ctr, round(t1.buy/t1.imp,6) btr, round(t1.order_num/t1.imp,6) salerate 
from (
    select category_value, strategy, platform,
    sum(click_num) click, sum(business_click_num) buy, sum(exposure_click_num) imp, 
    sum(order_items) order_items, sum(order_num) order_num
    from dm.dm_view_abtest_statistics
    where create_day between '%s' and '%s' and strategy in ('%s')
    group by category_value, strategy, platform
) t1
order by t1.category_value,t1.platform , t1.strategy;
"""
hive_sql_total = """
set tez.grouping.split-count=1;
set hive.exec.reducers.max=1;
set tez.am.resource.memory.mb=1024;
set hive.tez.container.size=1024;
set tez.runtime.io.sort.mb=400;
select t1.platform, t1.strategy, t1.click,t1.buy,t1.imp, t1.order_num, round(t1.click/t1.imp,6) ctr, round(t1.buy/t1.imp,6) btr, round(t1.order_num/t1.imp,6) salerate 
from (
    select strategy, platform,
    sum(click_num) click, sum(business_click_num) buy, sum(exposure_click_num) imp, 
    sum(order_items) order_items, sum(order_num) order_num
    from dm.dm_view_abtest_statistics
    where create_day between '%s' and '%s' and strategy in ('%s')
    group by strategy, platform
) t1;
"""

"""
操作流程：
su hive
1.@dn1上
    cd /home/opt/scripts/datasync/sqoop/shell
    sh -x order_history.sh order_history dw       
    跑订单数据
    
2.@dn1上，
    cd /home/opt/scripts/datawarehouse/shell/abtest/
    修改内容（时间、分类等）
    sh -x dwb_deal_abtest_statistics_detail.sh 明细表
    sh -x dm_view_abtest_statistics.sh         聚合表
    
3.执行上面的hive_sql
"""
day1, day2 = "2021-06-09", "2021-06-15"
strategies = ['deal_ctr_merged_tags', 'related_tags_mixed', 'rectab_related_tags_mixed']
print(hive_sql_total % (day1, day2, "','".join(strategies)))
print()
print(hive_sql_detail % (day1, day2, "','".join(strategies)))
