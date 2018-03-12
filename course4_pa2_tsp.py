# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 19:49
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course4_pa2_tsp.py
# @Software: PyCharm
import itertools
import functools
import math
import time

def readfile():
    with open('tsp.txt') as f:
        a = f.readlines()
        cities = {}
        counter = 1
        for line in a[1:]:
            cities[counter] = tuple(map(float, line.strip().split(' ')))
            counter = counter + 1
        return cities

def initodd(num, size):
    odd = {}
    inf = float("inf")
    temp = itertools.combinations(range(1, num+1), size)
    for i in range(1, num+1):
        for sub1 in temp:
            odd[sub1, i] = inf
    return odd

def initeven(num, size):
    even = {}
    inf = float("inf")
    temp = itertools.combinations(range(1, num + 1), size)
    for i in range(1, num + 1):
        for sub1 in temp:
            even[sub1, i] = inf
    return even

def tsp(num, start,cities):
    end = 1
    size = 1
    inf = float("inf")
    odd = {}
    even = {}
    for sub1 in itertools.combinations(range(1, num + 1), size):
        if sub1 == (1,):
            odd[sub1, end] = 0
        else:
            odd[sub1, end] = inf

    for size in range(2, num + 1):
        if size % 2:
            odd = initodd(num, size)
            for sub in filter(lambda x: start in x, itertools.combinations(range(1, num+1), size)):
                for end in filter(lambda x: x != start, sub):
                    temp = []
                    for k in filter(lambda y: y != end, sub):
                        temp.append(even[tuple(filter(lambda x: x != end, sub)), k] + math.sqrt((cities[k][0]-cities[end][0])**2+(cities[k][1]-cities[end][1])**2))
                    odd[sub, end] = min(temp)
        else:
            even = initeven(num, size)
            for sub in filter(lambda x: start in x, itertools.combinations(range(1, num+1), size)):
                for end in filter(lambda x: x != start, sub):
                    temp = []
                    for k in filter(lambda y: y != end, sub):
                        temp.append(odd[tuple(filter(lambda x: x != end, sub)), k] + math.sqrt((cities[k][0]-cities[end][0])**2+(cities[k][1]-cities[end][1])**2))
                    even[sub, end] = min(temp)
        print(size)
    if num % 2:
        return odd
    else:
        return even

def main():
    starttime = time.time()
    cities = readfile()
    num = 25
    start = 1
    bigmap = tsp(num, start, cities)
    smallmap = {}
    for i in range(1, num+1):
        smallmap[i] = bigmap[tuple(range(1, num+1)), i] + math.sqrt((cities[start][0]-cities[i][0])**2+(cities[start][1]-cities[i][1])**2)
    print(smallmap)
    print(smallmap[functools.reduce(lambda x, y: x if smallmap[x] < smallmap[y] else y, smallmap)])
    print(time.time() - starttime)

main()