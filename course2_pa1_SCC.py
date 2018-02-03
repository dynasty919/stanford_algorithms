# -*- coding: utf-8 -*-
# @Time    : 2018/2/3 19:18
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course2_pa1_SCC.py
# @Software: PyCharm
import sys
import threading

global counter                                            #定义两个全局变量，没办法必须要有，配合dict的
global leader

def initcounter():
    global counter
    counter = 1

def addcounter():
    global counter
    counter = counter + 1

def setleader(x):
    global leader
    leader = x

stack = {}                                                  #三个全局的dict，其中一个是最后得到的SCC结果，没办法必须要用dict
finish = {}                                                 #如果用list的话会慢到令人发指
result = {}
for a in range(1, 875715):
    stack[str(a)] = False
    finish[a] = ''

def readfile():
    '''
    读文件，时间会很漫长。。。因为数据大成一坨屎了
    '''
    with open('SCC.txt','rt') as f:
        a = f.readlines()
        b = []
        for c in a:
            b.append(c.strip().split(' '))
        graph = {}
        for d in b:
            if not d[0] in graph:
                graph[d[0]] = [d[1]]
            else:
                graph[d[0]].append(d[1])
        reversegraph = {}
        for e in b:
            if not e[1] in reversegraph:
                reversegraph[e[1]] = [e[0]]
            else:
                reversegraph[e[1]].append(e[0])
        return (graph,reversegraph)

def dfs1(graph, node):
    '''
    第一次DFS。
    '''
    stack[node] = True
    if not node in graph:
        finish[counter] = node
        addcounter()
    else:
        for a in graph[node]:
            if not stack[a]:
                dfs1(graph, a)
        finish[counter] = node
        addcounter()

def dfs2(graph, node):
    '''
    第二次DFS，这里我把stack这个hashmap重新用了一遍。最后得到的result的就是我们需要的SCC集合，虽然result在全局里。
    '''
    stack[node] = False
    if not leader in result:
        result[leader] = [leader]
    else:
        result[leader].append(node)
    if not node in graph:
        pass
    else:
        for a in graph[node]:
            if stack[a]:
                dfs2(graph, a)

def SCC():
    '''
    主程序，基本就是做两大轮的DFS，第二轮用到了第一轮生成的finish这个hashmap
    '''
    (graph, reversegraph) = readfile()
    initcounter()
    for a in range(1, 875715):
        if not stack[str(a)]:
            dfs1(reversegraph, str(a))

    for b in range(875714, 0, -1):
        if stack[finish[b]]:
            setleader(finish[b])
            dfs2(graph, finish[b])

def main():
    '''
    因为要求的是规模排名前五的SCC，所以放在这里求了。下面那一坨东西是跟人学的，用来解除python的递归次数限制的，原理不明。。。
    '''
    SCC()
    table = []
    for a in result:
        table.append(len(set(result[a])))
    for b in range(5):
        print(sorted(table, reverse=True)[b])

if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()