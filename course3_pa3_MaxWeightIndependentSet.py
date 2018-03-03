# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 17:41
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa3_mwis.py
# @Software: PyCharm
def readfile():
    with open('mwis.txt', 'rt') as f:
        a = f.readlines()
        c =[]
        for b in a[1:]:
            c.append(int(b.strip()))
        return c


def max_weight():
    intlist = readfile()
    maxweight = {}
    maxweight[-1] = 0
    maxweight[0] = 0
    maxweight[1] = intlist[0]
    for i in range(2,len(intlist)+1):
        maxweight[i] = max(maxweight[i-1], maxweight[i-2]+intlist[i-1])
    # print(maxweight)
    # print(len(intlist))
    return maxweight,intlist

def mwis():
    maxweight, intlist = max_weight()
    i = 1000
    set = {}
    while i >= 1:
        if maxweight[i-1] >= maxweight[i-2] + intlist[i-1]:
            i = i - 1
        else:
            set[i] = intlist[i-1]
            i = i - 2
    return set

def main():
    resultset = mwis()
    print(resultset)
    for iter in [1, 2, 3, 4, 17, 117, 517, 997]:
        if iter in resultset:
            print(str(iter) + " in the set")
        else:
            print(str(iter) + " NOT in the set")

main()