snapshot = """
snapshot '%s' ,'%s_snap'
"""
get_snapshot = """
hdfs dfs -ls hdfs://dealmoonCluster/apps/hbase/data/.hbase-snapshot | grep %s_snap
"""
get_snapshot2 = """
hdfs dfs -ls hdfs://dealmoonCluster/apps/hbase/data/.hbase-snapshot/%s_snap
"""
scp = """
hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot -Dmapreduce.map.memory.mb=4096 -Dmapreduce.map.java.opts=-Xmx8092m -Dsnapshot.export.buffer.size=65536 --snapshot %s_snap --copy-from hdfs://10.0.20.31:8020/apps/hbase/data --copy-to hdfs://10.111.11.201:8020/apps/hbase/data --mappers 5 --bandwidth 25 -overwrite
"""
scp2 = """
hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot -Dmapreduce.map.memory.mb=4096 -Dmapreduce.map.java.opts=-Xmx8092m -Dsnapshot.export.buffer.size=65536 --snapshot %s_snap --copy-from hdfs://10.0.20.31:8020/apps/hbase/data --copy-to hdfs://10.111.11.201:8020/apps/hbase/data --mappers 5 --bandwidth 25 -overwrite
"""
clone_snapshot = """
clone_snapshot '%s_snap','%s'
"""
disable = """
disable '%s'
"""
restore_snap = """
restore_snapshot '%s_snap'
"""
enable = """
enable '%s'
"""
delete = """
delete_snapshot '%s_snap'
"""

table_name = "ugc_guide_c"
if __name__ == '__main__':
	print(snapshot.strip() % (table_name, table_name))
	print(get_snapshot.strip() % table_name)
	print(get_snapshot2.strip() % table_name)
	print(scp.strip() % table_name)
	print(scp2.strip() % table_name)
	print(clone_snapshot.strip() % (table_name, table_name))
	print(disable.strip() % table_name)
	print(restore_snap.strip() % table_name)
	print(enable.strip() % table_name)
	print(delete.strip() % table_name)
