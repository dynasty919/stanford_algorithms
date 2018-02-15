# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 18:14
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course2_pa2_dijkstra.py
# @Software: PyCharm
import sys
import threading

def readfile():
    with open('Median.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for iter1 in a:
            b.append(int(iter1.strip()))
        return b

def heapmin_insert(heapmin, xint):
    def pop_up(heapmin, n):
        if n == 1:
            return heapmin
        else:
            if n % 2:
                if heapmin[n - 1] > heapmin[n // 2 - 1]:
                    return heapmin
                else:
                    heapmin[n - 1], heapmin[n // 2 - 1] = heapmin[n // 2 - 1], heapmin[n - 1]
                    return pop_up(heapmin, n // 2)
            else:
                if heapmin[n - 1] > heapmin[(n - 1) // 2]:
                    return heapmin
                else:
                    heapmin[n - 1], heapmin[(n - 1) // 2] = heapmin[(n - 1) // 2], heapmin[n - 1]
                    return pop_up(heapmin, (n + 1) // 2)
    if not heapmin:
        heapmin.append(xint)
        return heapmin
    else:
        heapmin.append(xint)
        heapmin = pop_up(heapmin, len(heapmin))
        return heapmin

def heapmax_insert(heapmax, xint):
    def pop_up(heapmax, n):
        if n == 1:
            return heapmax
        else:
            if n % 2:
                if heapmax[n - 1] < heapmax[n // 2 - 1]:
                    return heapmax
                else:
                    heapmax[n - 1], heapmax[n // 2 - 1] = heapmax[n // 2 - 1], heapmax[n - 1]
                    return pop_up(heapmax, n // 2)
            else:
                if heapmax[n - 1] < heapmax[(n - 1) // 2]:
                    return heapmax
                else:
                    heapmax[n - 1], heapmax[(n - 1) // 2] = heapmax[(n - 1) // 2], heapmax[n - 1]
                    return pop_up(heapmax, (n + 1) // 2)
    if not heapmax:
        heapmax.append(xint)
        return heapmax
    else:
        heapmax.append(xint)
        heapmax = pop_up(heapmax, len(heapmax))
        return heapmax

def heapmin_extract(heapmin):
    def pop_down(heapmin, n):
        if 2*n > len(heapmin):
            return heapmin
        elif 2*n == len(heapmin):
            if heapmin[n-1] > heapmin[2*n-1]:
                heapmin[n-1], heapmin[2*n-1] = heapmin[2*n-1], heapmin[n-1]
                return pop_down(heapmin, 2*n)
            else:
                return heapmin
        else:
            if heapmin[n-1] < heapmin[2*n-1] and heapmin[n-1] < heapmin[2*n]:
                return heapmin
            elif heapmin[n-1] > heapmin[2*n-1] and heapmin[n-1] < heapmin[2*n]:
                heapmin[n - 1], heapmin[2 * n - 1] = heapmin[2 * n - 1], heapmin[n - 1]
                return pop_down(heapmin, 2 * n)
            elif heapmin[n-1] > heapmin[2*n] and heapmin[n-1] < heapmin[2*n-1]:
                heapmin[n - 1], heapmin[2 * n] = heapmin[2 * n], heapmin[n - 1]
                return pop_down(heapmin, 2*n+1)
            else:
                if heapmin[2*n-1] < heapmin[2*n]:
                    heapmin[n - 1], heapmin[2 * n - 1] = heapmin[2 * n - 1], heapmin[n - 1]
                    return pop_down(heapmin, 2 * n)
                else:
                    heapmin[n - 1], heapmin[2 * n] = heapmin[2 * n], heapmin[n - 1]
                    return pop_down(heapmin, 2 * n + 1)
    heapmin[0] = heapmin[-1]
    heapmin.pop()
    heapmin = pop_down(heapmin, 1)
    return heapmin

def heapmax_extract(heapmax):
    def pop_down(heapmax, n):
        if 2*n > len(heapmax):
            return heapmax
        elif 2*n == len(heapmax):
            if heapmax[n-1] < heapmax[2*n-1]:
                heapmax[n-1], heapmax[2*n-1] = heapmax[2*n-1], heapmax[n-1]
                return pop_down(heapmax, 2*n)
            else:
                return heapmax
        else:
            if heapmax[n-1] > heapmax[2*n-1] and heapmax[n-1] > heapmax[2*n]:
                return heapmax
            elif heapmax[n-1] < heapmax[2*n-1] and heapmax[n-1] > heapmax[2*n]:
                heapmax[n - 1], heapmax[2 * n - 1] = heapmax[2 * n - 1], heapmax[n - 1]
                return pop_down(heapmax, 2 * n)
            elif heapmax[n-1] < heapmax[2*n] and heapmax[n-1] > heapmax[2*n-1]:
                heapmax[n - 1], heapmax[2 * n] = heapmax[2 * n], heapmax[n - 1]
                return pop_down(heapmax, 2*n+1)
            else:
                if heapmax[2*n-1] > heapmax[2*n]:
                    heapmax[n - 1], heapmax[2 * n - 1] = heapmax[2 * n - 1], heapmax[n - 1]
                    return pop_down(heapmax, 2 * n)
                else:
                    heapmax[n - 1], heapmax[2 * n] = heapmax[2 * n], heapmax[n - 1]
                    return pop_down(heapmax, 2 * n + 1)
    heapmax[0] = heapmax[-1]
    heapmax.pop()
    heapmax = pop_down(heapmax, 1)
    return heapmax

def two_heaps(heapmax, heapmin, xint):
    if heapmax == []:
        heapmax.append(xint)
        return (heapmax, heapmin, xint)
    else:
        if len(heapmax) == len(heapmin):
            if xint < heapmin[0]:
                heapmax = heapmax_insert(heapmax, xint)
                return (heapmax, heapmin, heapmax[0])
            else:
                heapmax = heapmax_insert(heapmax, heapmin[0])
                heapmin = heapmin_extract(heapmin)
                heapmin = heapmin_insert(heapmin, xint)
                return (heapmax, heapmin, heapmax[0])
        elif len(heapmax) > len(heapmin):
            if xint > heapmax[0]:
                heapmin = heapmin_insert(heapmin, xint)
                return (heapmax, heapmin, heapmax[0])
            else:
                heapmin = heapmin_insert(heapmin, heapmax[0])
                heapmax = heapmax_extract(heapmax)
                heapmax = heapmax_insert(heapmax, xint)
                return (heapmax, heapmin, heapmax[0])
        else:
            print('error')

def median_heap():
    stream = readfile()
    result = []
    heapmin = []
    heapmax = []
    for iter2 in stream:
        (heapmax, heapmin, mid) = two_heaps(heapmax, heapmin, iter2)
        result.append(mid)
    print(result)
    return sum(result)

def main():
    print(median_heap())

main()
