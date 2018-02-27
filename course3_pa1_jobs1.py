# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 14:48
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course3_pa1_jobs1.py
# @Software: PyCharm

def readfile():
    with open('jobs.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(c.strip().split(' '))
        return b

def order():
    jobs = readfile()
    temp = sorted(jobs, key=lambda iter1: int(iter1[0]), reverse=True)
    orderlist = sorted(temp, key=lambda iter2: int(iter2[0])-int(iter2[1]), reverse=True)
    return orderlist

def main():
    orderlist = order()
    print(orderlist)
    temp = [0]
    result = 0
    for num in range(len(orderlist)):
        temp.append(int(orderlist[num][1])+int(temp[num]))
    for num2 in range(len(orderlist)):
        result = result + int(orderlist[num2][0])*temp[num2+1]
    print(result)

main()