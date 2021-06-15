import time

import tables


def snapshot_scripts(tbs=[]):
    print('快照全量执行')
    # 全量表的shell脚本
    if len(tbs) == 0:
        tbs1, tbs2 = parse(tables.small_tables), parse(tables.big_tables)
        tbs1.extend(tbs2)
        tbs = tbs1
        del tbs2
    # 1.创建快照
    snapshot = """
    snapshot '%s' ,'%s_snap'
    """.strip()
    print_old()
    for t in tbs: print(snapshot % (t, t))
    print_new()
    # 2.copy快照
    scp = """
    hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot -Dmapreduce.map.memory.mb=2048 -Dmapreduce.map.java.opts=-Xmx8092m -Dsnapshot.export.buffer.size=65536 --snapshot %s_snap --copy-from hdfs://10.0.20.31:8020/apps/hbase/data --copy-to hdfs://10.111.11.201:8020/apps/hbase/data --mappers 4 --bandwidth 25 -overwrite
    """.strip()
    for t in tbs: print(scp % t)

    drop = """
    drop '%s'
    """.strip()

    # 3.clone快照
    clone_snapshot = """
    clone_snapshot '%s_snap','%s'
    """.strip()
    # 4.disable table
    disable = """
    disable '%s'
    """.strip()
    # 5.restore_snapshot
    restore_snap = """
    restore_snapshot '%s_snap'
    """.strip()
    # 6.enable 'ugc_guide_c'
    enable = """
    enable '%s'
    """.strip()
    # 7.delete_snapshot 'ugc_guide_c_snap'
    delete = """
    delete_snapshot '%s_snap'
    """.strip()
    # 8.limit 1
    scan = """
    scan '%s',{LIMIT=>1}
    """.strip()
    print_new()
    for t in tbs:
        print()
        print(disable % t)
        print(drop % t)
        print(clone_snapshot % (t, t))
        print(disable % t)
        print(restore_snap % t)
        print(enable % t)
        print(delete % t)
        print(scan % t)


def incr_scripts():
    print('增量执行')
    # 增量表的shell脚本
    tbs = [
        ['au_ugc_guide_u', '1621579542383'],
        ['ugc_guide_c', '1621238610000'],
        ['deal_click_info_2021', '1621237614000'],
        ['ugc_guide_u', '1621238640000'],
        ['ugc_post_c', '1621238676000'],
        ['ugc_post_u', '1621245443000'],
    ]
    now = str(int(time.time()) * 1000)
    export_fmt = """
    hbase org.apache.hadoop.hbase.mapreduce.Export -Dhbase.export.scanner.batch=2000 -D mapred.output.compress=true %s hdfs://10.111.11.201:8020/migrate/hbase/%s 1 %s %s
    """.strip()
    import_fmt = """
    hbase org.apache.hadoop.hbase.mapreduce.Driver import %s hdfs://10.111.11.201:8020/migrate/hbase/%s/*
    """.strip()
    print_old()
    for t in tbs: print(export_fmt % (t[0], t[0], t[1], now))
    print_new()
    for t in tbs: print(import_fmt % (t[0], t[0]))


def print_old():
    print("--------------------------老集群--------------------------")


def print_new():
    print("==========================新集群==========================")


def parse(s):
    tbs = []
    for x in s.split('\n'):
        tb = x.split('/')[-1].split(' ')[0].strip()
        if tb:
            tbs.append(tb)
        else:
            print(tb)
    return tbs


if __name__ == '__main__':
    # incr_scripts()
    snapshot_scripts(['deal_click_info_2021'])
