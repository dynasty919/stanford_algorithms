# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 16:06
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course4_pa1_floyd-warshall.py
# @Software: PyCharm
import time

def readfile():
    with open('g3.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(c.strip().split(' '))
        d = {}
        for e in b:
            d[(int(e[0]), int(e[1]))] = int(e[2])
        return d

def floyd_warshall(num, graph):
    odd = {}
    even = {}
    inf = float("inf")
    for i in range(1, num):
        for j in range(1, num):
            if i == j:
                even[(i, j, 0)] = 0
            elif (i, j) in graph:
                even[(i, j, 0)] = graph[(i, j)]
            else:
                even[(i, j, 0)] = inf
    for k in range(1, num):
        if k%2:
            odd = {}
            for i in range(1, num):
                for j in range(1, num):
                    odd[(i, j, k)] = min(even[(i, j, k-1)], even[(i, k, k-1)]+even[(k, j, k-1)])
                    if i == j:
                        if odd[(i, i, k)] < 0:
                            return "fuck"
        else:
            even = {}
            for i in range(1, num):
                for j in range(1, num):
                    even[(i, j, k)] = min(odd[(i, j, k-1)], odd[(i, k, k-1)]+odd[(k, j, k-1)])
                    if i == j:
                        if even[(i, i, k)] < 0:
                            return "fuck"
        print(k)
    if num%2:
        return even
    else:
        return odd

def main():
    start = time.time()
    graph = readfile()
    num = 1000 + 1
    result = floyd_warshall(num, graph)
    if type(result) == dict:
        resultnum = {}
        for i in range(1, num):
            for j in range(1, num):
                resultnum[result[(i, j, num-1)]] = (i, j)
        print(min(resultnum))
    else:
        print("the graph have negative cycle")
    print(time.time() - start)

main()

