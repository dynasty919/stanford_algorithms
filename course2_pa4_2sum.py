# -*- coding: utf-8 -*-
# @Time    : 2018/2/20 0:54
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : coursera2_pa4_2sum.py
# @Software: PyCharm
import bisect

def readfile():
    with open('2sum.txt', 'rt') as f:
        a = f.readlines()
        b = []
        for iter1 in a:
            b.append(int(iter1.strip()))
        return b

def main():
    '''
    这题实际上就是LeetCode里面那个twosum，不过这里用hash table求的话实在太费时，所以我用二叉树搜索求的。。。
    '''
    xlist = sorted(readfile())
    templist = []
    for num1 in xlist:
        left = bisect.bisect_left(xlist, -10000-num1)
        right = bisect.bisect_right(xlist, 10000-num1)
        if right > left:
            for num2 in xlist[left:right]:
                templist.append((num1, num2))
    resultlist = []
    for iter2 in templist:
        if not iter2[0] == iter2[1]:
            resultlist.append(iter2[0]+iter2[1])
    print(len(set(resultlist)))

main()