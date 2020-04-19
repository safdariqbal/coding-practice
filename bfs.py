#!/usr/bin/env python2

from collections import deque

class Node:
    
    def __init__(self, label):
        self.label = label
        self.distance = -1
        #self.processed = False
        self.discovered = False
        self.neighbors = []
        
class Graph:
    
    def __init__(self, n):         
        self.nodes = [None]*n
        for i in xrange(0, n):
            self.nodes[i] = Node(i)
        self.edges = 0
    
    def connect(self, u, v):
        self.nodes[u].neighbors.append(self.nodes[v])
        self.nodes[v].neighbors.append(self.nodes[u])
        self.edges += 1
    
    def do_bfs(self, s):
        queue = deque()
        
        S = self.nodes[s]
        S.distance = 0
        S.discovered = True
        queue.appendleft(S)
        while len(queue) > 0:
            qn = queue.pop()
            print qn
            for nn in qn.neighbors:
                if not nn.discovered:
                    nn.discovered = True
                    nn.distance = qn.distance + 6
                    queue.appendleft(nn)
        
    def find_all_distances(self, s):
        self.do_bfs(s)
        for i in self.nodes:
            if i.label != s:
                print i.distance,
        print

t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
