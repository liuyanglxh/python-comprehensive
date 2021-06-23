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

# 策略的名字
strategy_name = {
	"deal_ctr_merged_tags": "浏览历史Tag推荐",
	"related_tags_mixed": "浏览历史Tag+相关Tag混合推荐",
	"rectab_related_tags_mixed": "浏览历史Tag+相关Tag混合推荐"
}

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
    select t2.strategy as strategy, t2.platform as platform,
    sum(t2.click_num) click, sum(t2.business_click_num) buy, sum(t2.exposure_click_num) imp, 
    sum(t2.order_items) order_items, sum(t2.order_num) order_num
    from (
		select %s as strategy,platform,click_num,business_click_num,exposure_click_num,order_items,order_num
		from dm.dm_view_abtest_statistics
		where create_day between '%s' and '%s' and strategy in ('%s')
    ) t2
    group by t2.strategy, t2.platform
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


def print_sql(day1, day2, strategies):
	mapping = [
		"when strategy = '%s' then '%s'" % (x, strategy_name[x])
		for x in strategies
	]
	strategy_mapping = """
		case %s end
		""".strip() % ' '.join(mapping)
	print("总数")
	total_sql = hive_sql_total % (strategy_mapping, day1, day2, "','".join(strategies))
	print(total_sql.replace('\t', ' '))
	print("详情")
	print(hive_sql_detail % (day1, day2, "','".join(strategies)))


day1, day2 = "2021-06-09", "2021-06-15"
strategies = ['deal_ctr_merged_tags', 'related_tags_mixed', 'rectab_related_tags_mixed']

if __name__ == '__main__':
	print_sql(day1, day2, strategies)
