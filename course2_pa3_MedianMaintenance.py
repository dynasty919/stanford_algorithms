# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 18:14
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course2_pa2_dijkstra.py
# @Software: PyCharm

def readfile():
    with open('Median.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for iter1 in a:
            b.append(int(iter1.strip()))
        return b

heapmin = []
heapmax = []
global ismaxlonger

def init_ismaxlonger():
    global ismaxlonger
    ismaxlonger = False

def invert_ismaxlonger():
    global ismaxlonger
    ismaxlonger = not ismaxlonger

def heapmin_insert(xint):
    if not heapmin:
        heapmin.append(xint)
    else:
        heapmin.append(xint)
        pop_up(heapmin.index(xint))


def two_heaps(xint):
    invert_ismaxlonger()
    if ismaxlonger:
        if xint > heapmax[0]:
            heapmin_insert(xint)
        else:
            heapmin_insert(heap_extract[0])
            heapmax_extract()
            heapmax_insert(xint)
    else:
        if xint > heapmin[0]:
            heapmax_insert(heapmin[0])
            heapmin_extract()
            heapmin_insert(xint)
        else:
            heapmax_insert(xint)
    return heapmax[0]



def median_heap():
    stream = readfile()
    result1 = []
    init_ismaxlonger()
    for iter2 in stream:
        result1.append(two_heaps(iter2))
    return sum(result1)%10000