# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 16:05
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa4_knapsack1.py
# @Software: PyCharm
def readfile():
    with open('knapsack1.txt', 'rt') as f:
        a = f.readlines()
        c = []
        for b in a[1:]:
            c.append(b.strip().split(' '))
        d = list(map(lambda x: (int(x[0]), int(x[1])), c))
        return d

def knapsack():
    stuff = readfile()
    arrange = {}
    for aint in range(10001):
        arrange[(0, aint)] = 0
    for stuffnum in range(1,101):
        for weightnum in range(10001):
            if weightnum-stuff[stuffnum-1][1] >= 0:
                arrange[(stuffnum, weightnum)] = max(arrange[(stuffnum-1, weightnum)], arrange[(stuffnum-1, weightnum-stuff[stuffnum-1][1])]+stuff[stuffnum-1][0])
            else:
                arrange[(stuffnum, weightnum)] = arrange[(stuffnum-1, weightnum)]
    print(arrange)
    return arrange[(100, 10000)]

def main():
    print(knapsack())

main()