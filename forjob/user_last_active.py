# coding=utf-8
import json
import os
import time

"""
君祺的需求
"""


def __format_day__(seconds, fmt='%y-%m-%d'):
    if seconds is None: return '最近60天未查到数据'
    return time.strftime(fmt, time.localtime(seconds))


def rm_dir(path):
    if not path.endswith("/"): path += "/"
    for filename in os.listdir(path):
        all_path = path + "/" + filename
        print('remove', all_path)
        os.remove(all_path)


def read_dir(path, handle_line):
    """
    读取目录下的所有文件内容
    """
    if not path.endswith("/"): path += "/"
    for filename in os.listdir(path):
        all_path = path + "/" + filename
        read_file(all_path, handle_line)


def read_file(path, handle_line):
    """
    读取文件内容
    :param	处理line的函数
    """
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if not line: break
            if handle_line(line) == 'break':
                break


def analysis():
    userIds = {6018, 12624, 12976, 13200, 13933, 14697, 21370, 67676, 69607, 89018, 98453, 110158, 111505, 117394,
               132122,
               133177, 141064, 141630, 152613, 160337, 169231, 177404, 182780, 192300, 192328, 195126, 196738, 213114,
               224225, 228750, 239412, 241832, 241840, 246245, 249305, 252006, 261231, 353586, 375210, 398272, 404190,
               440767, 450351, 450968, 468415, 474637, 474919, 501228, 510977, 531795, 537587, 546131, 546462, 561030,
               572704, 587008, 596067, 604559, 622850, 627283, 627285, 686982, 688548, 690284, 707028, 707792, 716340,
               727507, 749416, 750755, 762277, 788589, 849950, 860211, 868808, 874055, 904364, 923255, 925731, 931369,
               997115, 1001572, 1022361, 1026528, 1083840, 1195188, 1199483, 1200305, 1227327, 1229875, 1276433,
               1290701,
               1290812, 1301814, 1310502, 1320149, 1399423, 1506133, 1508416, 1517300, 1535229}
    st = set()
    for x in userIds: st.add(x)

    result, total, tm = {}, 60, int(time.time())
    cmd_fmt = 'hdfs dfs -get /flume/biz.app/%s/*  /tmp/active/'

    def rd(line):
        row = json.loads(line)
        userId = int(row['value']['userId']) if 'value' in row and 'userId' in row['value'] and row['value'][
            'userId'] else 0
        if userId not in st: return
        tm = int(row['time'])
        result.setdefault(userId, 0)
        result[userId] = max(result[userId], tm)

    while total > 0 and len(result) < len(userIds):
        cmd = cmd_fmt % __format_day__(tm)
        print('still need', len(userIds) - len(result))
        print(cmd)
        os.system(cmd)
        read_dir('/tmp/active/', rd)
        total -= 1
        tm -= 24 * 60 * 60
        rm_dir('/tmp/active')

    userLastTime = [__format_day__(result.get(uId)) for uId in userIds]

    for x in userLastTime:
        print(x)


if __name__ == '__main__':
    analysis()
