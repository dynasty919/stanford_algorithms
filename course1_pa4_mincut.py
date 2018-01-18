# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 2:04
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course1_pa4_mincut.py
# @Software: PyCharm
import random

def readfile():
    '''
    读取文件中的数据，注意对文件里的数据格式是有要求的
    '''
    try:
        f = open('kargerMinCut.txt', 'r')
        a = f.readlines()
        c =[]
        for b in a:
            c.append(b.strip().split('\t'))
        result ={}
        for d in c:
            result[d[0]] = d[1:]
        return result
    finally:
        if f:
            f.close()

def randomcut(adict):
    '''
    生成两个随机数，返回随机数决定的两个字符串
    '''
    a = random.randrange(0, len(adict))
    b = random.randrange(0, len(adict[list(adict.keys())[a]]))
    return (list(adict.keys())[a], adict[list(adict.keys())[a]][b])


def newadict(adict, vertex1, vertex2):
    '''
    把随机决定的那两个字符串代表的结点融合（这个模块写的简直要了老命了）
    '''
    list1 = adict[vertex1][:]
    list2 = adict[vertex2][:]
    for i in list1:
        if i == vertex2:
            adict[vertex1].remove(i)
    for j in list2:
        if j == vertex1:
            adict[vertex2].remove(j)

    for a in adict[vertex2]:
        if a != vertex1 :
            for m in adict[a]:
                if m == vertex2:
                    adict[a].remove(vertex2)
                    adict[a].append(vertex1)
                    adict[vertex1].append(a)

    adict.pop(vertex2)
    return adict


def mincut(adict):
    '''
    主程序，融合到只剩两个结点的时候停止
    '''
    if len(adict) == 2:
        return (len(adict[list(adict.keys())[0]]), len(adict[list(adict.keys())[1]]), adict)
    else:
        (vertex1, vertex2) = randomcut(adict)
        adict2 = newadict(adict, vertex1, vertex2)
        return mincut(adict2)


def main():
    '''
    运行100次主程序，返回最小的mincut
    '''
    templist = []
    for a in range(100):
        adict = readfile()
        templist.append(mincut(adict)[0])
    print(templist)
    print(min(templist))

main()


