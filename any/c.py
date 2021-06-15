export_fmt = """
hbase org.apache.hadoop.hbase.mapreduce.Export -Dhbase.export.scanner.batch=2000 -D mapred.output.compress=true %s hdfs://10.111.11.201:8020/migrate/hbase/%s 
""".strip()
import_fmt = """
hbase org.apache.hadoop.hbase.mapreduce.Driver import %s hdfs://10.111.11.201:8020/migrate/hbase/%s/*
""".strip()
cnt_fmt = """
hbase org.apache.hadoop.hbase.mapreduce.RowCounter '%s'
""".strip()
create_fmt = """
create '%s','cf' 
""".strip()

tbl = "ugc_guide_u"

print(export_fmt % (tbl, tbl))
print(create_fmt % tbl)
print(import_fmt % (tbl, tbl))
print(cnt_fmt % tbl)
