
def addedge(a,b):
    v[a].append(b)
    v[b].append(a)

v = []

edgenum = 8

for _ in range(edgenum):
    v.append([])

# 貝本 15.3
addedge(0,2)
addedge(0,1)
addedge(1,2)
addedge(1,3)
addedge(2,3)
addedge(3,4)
addedge(4,5)
addedge(4,6)
addedge(4,7)
addedge(5,7)

INTMAX = 1 << 63

visitednum = [None] * edgenum
lowest = [INTMAX] * edgenum
parent = [None] * edgenum

import collections
q = collections.deque([])

q.append([0, -1]) # node, parent
timer = 1

while len(q) > 0:
    curnode, parentnode = q.pop()
    visitednum[curnode] = lowest[curnode] = timer
    for nextNode in v[curnode]:
        if visitednum[nextNode] is not None:
            parent[nextNode] = curnode
            q.append([nextNode, curnode])



