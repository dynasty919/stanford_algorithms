# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 0:45
# @Author  : dynasty919
# @Email   : dynasty919@163.com
# @File    : course4_pa4_2sat-scc.py
# @Software: PyCharm
from time import time
from itertools import groupby
from collections import defaultdict

class Tracker(object):
    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()

def dfs(graph_dict, node, tracker):
    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time

def dfs_loop(graph_dict, nodes, tracker):
    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs(graph_dict, node, tracker)

def graph_reverse(graph):
    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph

def scc(graph):
    out = defaultdict(list)
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reversed_graph, nodes, tracker1)
    sorted_nodes = sorted(tracker1.finish_time,
                          key=tracker1.finish_time.get, reverse=True)
    dfs_loop(graph, sorted_nodes, tracker2)
    for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                key=tracker2.leader.get):
        out[lead] = list(vertex)
    return out

def two_sat(graph):
    groups = scc(graph)
    for group in groups.values():
        group = set(group)
        for node in group:
            if -node in group:
                return 0
    return 1

def main():
    result = []
    for i in range(1, 7):
        graph = defaultdict(list)
        with open("2sat%s.txt" % i) as file_in:
            next(file_in)
            for line in file_in:
                x1, x2 = map(int, line.strip().split(' '))
                graph[-x1].append(x2)
                graph[-x2].append(x1)
        result.append(two_sat(graph))
        del graph
    return result

if __name__ == "__main__":
    start = time()
    print(main())
    print(time() - start)