# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 20:20
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course1_pa3_quicksort2.py
# @Software: PyCharm
#quicksort when we always choose pivot as the last data
def read_file():
    try:
        f = open('QuickSort.txt', 'r')
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

def quicksort(l, start, end):
    if start >= end :
        return (l,0)
    else:
        (middle, num1) = partition(l, start, end)
        (l, num2) = quicksort(l, start, middle)
        (l, num3) = quicksort(l, middle + 1, end)
        return (l,num1 + num2 + num3)


def partition(l, start, end):
    count = 0
    l[end-1], l[start] = l[start], l[end-1]
    i = start+1
    for j in range(start + 1, end):
        if l[j] > l[start]:
            count = count + 1
        if l[j] < l[start]:
            l[j], l[i] = l[i], l[j]
            i = i + 1
            count = count + 1
    l[i-1], l[start] = l[start], l[i-1]
    return (i-1, count)

def main():
    l = read_file()
    print(quicksort(l, 0, len(l)))

main()