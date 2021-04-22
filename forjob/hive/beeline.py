def cmd(sql, file) -> str:
	a = """
	    beeline -u "jdbc:hive2://master1:2181,master2:2181,slave1:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2" -nliuyang -pc2qGJ1GB --verbose=true  --showHeader=false --outputformat=csv2  --color=true  -e"set tez.grouping.split-count=1;set hive.exec.reducers.max=1;set tez.am.resource.memory.mb=1024;set hive.tez.container.size=1024;set tez.runtime.io.sort.mb=400;%s" > %s
	""" % (sql.strip().replace("\n", " "), file)
	return a.strip()


sql = """
select distinct udid,strategy from ods.ods_impression_log
where create_day between '2021-04-07' and '2021-04-20'
and type='deal' and rip='home_list' and scene = 'ad_list_new'
and (ad_type is not null and length(ad_type)>0)
"""
file = "/tmp/ly/abtest.csv"

if __name__ == '__main__':
	print(cmd(sql, file))
