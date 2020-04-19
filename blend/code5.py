class Node:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class IntervalTree:

    def __init__(self):
        self.root = Node(0,24)
    
    def __insert(self, node, start, end):
        if node.left == None:
            node.left = Node(start, end)
        else:
            if start <= node.left.start or (start > node.left.start and end < node.left.end) or (start < node.left.end and end > node.right.start):
                self.__insert(node.left)
            else:
                if node.right == None:
                    self.__insert(node.right)
                else:
                    node.right = Node(start, end)
        
    def insert(self, start, end):
        self.__insert(root, start, end)

    def find(self, start, end):
        pass

def freeSched(sched):
    sch_free = []
    for t in sched:
        if start != t[0]:
            ti = (start, t[0])
            sch_free.append(sch_free)
        start = t[1]
    return sch_free

def findTimes(schedules):

    sch = schedules[0]
    start = 0
    sch_free = freeSched(sch)
    tree = IntervalTree()

    for ti in sch_free:
        tree.insert(ti)

    result = []

    for s in schedules[1:n-1]:
        for ti in s:
            if tree.find(ti):
                tree.insert(ti)
    
    for s2 in schedules[-1]:
        for ti in s2:
            if tree.find(ti): 
                result.append(ti)       

    return result

