# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 2:49
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course4_pa3_tsp_big.py
# @Software: PyCharm
import functools
import math
import time

def readfile():
    with open('tsp_big.txt') as f:
        a = f.readlines()
        cities = {}
        counter = 1
        for line in a[1:]:
            cities[counter] = tuple(map(float, line.strip().split(' ')[1:]))
            counter = counter + 1
        return cities

def tsp_big():
    cities = readfile()
    start = 1
    startcordinate = cities[start]
    num = 33708
    visited = [1]
    distance = 0
    while len(visited) < num:
        nextcity = functools.reduce(lambda x, y: x if (cities[x][0]-cities[start][0])**2+(cities[x][1]-cities[start][1])**2 <= (cities[y][0]-cities[start][0])**2+(cities[y][1]-cities[start][1])**2 else y, filter(lambda x: x != start, cities))
        distance = distance + math.sqrt((cities[nextcity][0]-cities[start][0])**2+(cities[nextcity][1]-cities[start][1])**2)
        del cities[start]
        visited.append(nextcity)
        start = nextcity
        print(len(visited))
    return distance + math.sqrt((startcordinate[0]-cities[start][0])**2+(startcordinate[1]-cities[start][1])**2)

def main():
    start = time.time()
    print(tsp_big())
    print(time.time()-start)

if __name__ == "__main__":
    main()