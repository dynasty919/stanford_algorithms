# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 0:31
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course1_pa2_NumberOfInversions.py
# @Software: PyCharm
def read_file():
    try:
        f = open('IntegerArray.txt', 'r')
        a = f.readlines()
        # result = list(map(lambda x: x.strip(), a))
        result = []
        for b in a:
            result.append(int(b.strip()))
        return result
        f.close()
    finally:
        if f:
            f.close()

def sortandcount(a):
    if len(a) < 2:
        return (a, 0)
    else:
        i = len(a)//2
        (x, num1) = sortandcount(a[:i])
        (y, num2) = sortandcount(a[i:])
        (z, num3) = mergeandcount(x, y)
        return (z, num1 + num2 + num3)

def mergeandcount(l1, l2):
    a = 0
    b = 0
    count = 0
    result =[]
    while a < len(l1) and b < len(l2):
        if l1[a] < l2[b]:
            result.append(l1[a])
            a = a + 1
        else:
            result.append(l2[b])
            b = b + 1
            count = count + len(l1) - a
    if a < len(l1):
        result.extend(l1[a:])
    if b < len(l2):
        result.extend(l2[b:])
    return (result, count)

list = read_file()
print(sortandcount(list))

