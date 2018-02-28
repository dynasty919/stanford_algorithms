# -*- coding: utf-8 -*-
# @Time    : 2018/2/28 22:30
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : clustering.py
# @Software: PyCharm

def readfile():
    with open('clustering1.txt','rt') as f:
        a = f.readlines()
        b = []
        for c in a[1:]:
            b.append(c.strip().split(' '))
        f = sorted(b, key=lambda iter1: int(iter1[2]))
        d ={}
        for e in f:
            d[(e[0], e[1])] = int(e[2])
        return d

def greedy(verteces, distances):
    for dist in distances:
        if verteces[dist[0]] != verteces[dist[1]]:
            return dist

def clustering(distances):
    verteces = {}
    for iter in range(500):
        verteces[str(iter+1)] = iter + 1
    while len(set(verteces.values())) > 4:
        (vertex1, vertex2) = greedy(verteces, distances)
        temp = verteces[vertex2]
        for vertex in verteces:
            if verteces[vertex] == temp:
                verteces[vertex] = verteces[vertex1]
    return verteces

def main():
    distances = readfile()
    verteces = clustering(distances)
    print(distances)
    print(verteces)
    result = {}
    for v in verteces:
        if verteces[v] in result:
            result[verteces[v]].append(v)
        else:
            result[verteces[v]] = [v]
    print(result)
    maxdis = greedy(verteces, distances)
    print(maxdis)
    print(distances[maxdis])

main()