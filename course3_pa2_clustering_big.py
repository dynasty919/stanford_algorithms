# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 0:32
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa2_clustering_big.py
# @Software: PyCharm
from copy import deepcopy
import datetime

def readfile():
    with open('clustering_big.txt','rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(c.strip().split(' '))
        d = sorted(set(map(tuple, b)))
        f ={}
        g = 1
        for e in d:
            f[e] = g
            g = g + 1
        return f

verteces = readfile()
queue = []

def ifclose(vertex1,vertex2):
    count = 0
    for a in range(24):
        count = count + (int(vertex1[a]) ^ int(vertex2[a]))
    if count > 2:
        return False
    else:
        return True

def clustering_big():
    queue.append(list(verteces.keys())[0])
    del verteces[list(verteces.keys())[0]]
    while len(queue) > 0:
        flag = queue[0]
        queue.pop(0)
        temp = deepcopy(verteces)
        for v in temp:
            if ifclose(flag, v):
                del verteces[v]
                queue.append(v)


def main():
    count = 0
    while len(verteces) > 0:
        clustering_big()
        count = count + 1
        print(count)
    print(count)
    time_stamp = datetime.datetime.now()
    print("time_stamp       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))


main()