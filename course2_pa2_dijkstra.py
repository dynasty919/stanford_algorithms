# -*- coding: utf-8 -*-
# @Time    : 2018/2/10 23:50
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course2_pa2_dijkstra.py
# @Software: PyCharm
from copy import deepcopy

result = {'1':'0'}    #起点

def readfile():
    '''
    读文件
    '''
    with open('dijkstraData.txt', 'rt') as f:
        a = f.readlines()
        b =[]
        for iter1 in a:
            b.append(iter1.strip().split('\t'))
        result = {}
        for iter2 in b:
            result[iter2[0]] = list(map(lambda x: tuple(x.split(',')), iter2[1:]))
        return result

def greedy(ally, enemy):
    '''
    输入两个阵营图，通过比较greedy值找出适合劝降的地方阵营结点，返回该结点和其greedy值（什么greedy值...其实就是最小路径）
    '''
    target = ('', False)
    for tail in ally:
        for head in ally[tail]:
            if head[0] in enemy:
                if not target[1]:
                    target = head
                elif int(result[tail]) + int(head[1]) < int(target[1]):
                    target = (head[0], str(int(result[tail]) + int(head[1])))
    return target

def dijkstra():
    '''
    主程序，初始化几个dict后就开始while循环，直到所有点都被处理为止
    '''
    graph = readfile()
    ally = {}
    enemy = deepcopy(graph)
    ally['1'] = enemy['1']
    del enemy['1']
    while not ally == graph :
        (vertex, distance) = greedy(ally, enemy)
        ally[vertex] = enemy[vertex]
        del enemy[vertex]
        result[vertex] = distance
    return result

def main():
    '''
    输出所有点相对起点（'1')的最小路径
    '''
    distances = dijkstra()
    print(list(map(lambda x: (str(x), distances[str(x)]), sorted([*map(lambda y: int(y), distances.keys())]))))
    print([distances['7'], distances['37'], distances['59'], distances['82'], distances['99'], distances['115'], distances['133'], distances['165'], distances['188'], distances['197']])

main()