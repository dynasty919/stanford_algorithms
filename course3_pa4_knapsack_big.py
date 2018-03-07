# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 16:56
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa4_knapsack_big.py
# @Software: PyCharm
def readfile():
    with open('knapsack_big.txt', 'rt') as f:
        a = f.readlines()
        c = []
        for b in a[1:]:
            c.append(b.strip().split(' '))
        d = list(map(lambda x: (int(x[0]), int(x[1])), c))
        f = {}
        for e in range(2000):
            f[e] = d[e]
        return f

def knapsack():
    stuff = readfile()
    odd = {}
    for aint in range(2000001):
        odd[(0, aint)] = 0
    for stuffnum in range(1, 2001):
        if stuffnum % 2 == 1 :
            even = {}
            for weightnum in range(2000001):
                temp = weightnum - stuff[stuffnum - 1][1]
                if temp >= 0:
                    even[(stuffnum, weightnum)] = max(odd[(stuffnum - 1, weightnum)],odd[(stuffnum - 1, temp)] + stuff[stuffnum - 1][0])
                else:
                    even[(stuffnum, weightnum)] = odd[(stuffnum - 1, weightnum)]
        else:
            odd = {}
            for weightnum in range(2000001):
                temp = weightnum - stuff[stuffnum - 1][1]
                if temp >= 0:
                    odd[(stuffnum, weightnum)] = max(even[(stuffnum-1, weightnum)], even[(stuffnum-1, temp)]+stuff[stuffnum-1][0])
                else:
                    odd[(stuffnum, weightnum)] = even[(stuffnum-1, weightnum)]
    return odd[(2000, 2000000)]


def main():
    print(knapsack())

main()