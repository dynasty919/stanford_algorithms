# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 17:37
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa1_prim.py
# @Software: PyCharm
import functools

verteces = []  #本方阵营的结点集合
edges = []  #已加入最小生成树的边集合

def readfile():
    '''
    读文件，读完之后的图是以边集合的形式表示的，而不是一般的邻接表形式
    '''
    with open('edges.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(c.strip().split(' '))
        return b

def greedy(graph):
    '''
    while循环中的具体内容。greedy出此时权最小的符合要求（穿越敌我阵营）的边，然后更新两个全局list
    '''
    minedge = functools.reduce(lambda x, y: y if int(y[2]) < int(x[2]) and ((y[0] in verteces and not y[1] in verteces) or (y[0] not in verteces and y[1] in verteces)) else x, graph)
    if minedge[0] in verteces and not minedge[1] in verteces:
        verteces.append(minedge[1])
    else:
        verteces.append(minedge[0])
    edges.append(minedge)

def prim():
    '''
    主程序，先找出最小权的边以初始化两个全局list，然后开始while循环
    '''
    graph = readfile()
    minedge0 = functools.reduce(lambda x, y: x if int(x[2]) < int(y[2]) else y, graph)
    verteces.append(minedge0[0])
    verteces.append(minedge0[1])
    edges.append(minedge0)
    while len(verteces) < 500:
        greedy(graph)
    return edges

def main():
    '''
    得到边集合形式的MST之后，对其计算边的权之和
    '''
    result = prim()
    print(result)
    mincost = functools.reduce(lambda x, y: x+int(y[2]), result, 0)
    print(mincost)

main()