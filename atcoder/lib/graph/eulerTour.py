"""
   0
   |
 +-+--+
 1    |
|+|   |
2 4   5
|
3
"""
import sys

sys.setrecursionlimit(100000)

N = 7
G =[None] * N
# (next, cost)
G[0] = []
G[1] = [(2,1),(6,16)]
G[2] = [(3,2),(5,8)]
G[3] = [(4,4)]
G[4] = []
G[5] = []
G[6] = []

vertexCost = [None] * N
vertexCost = [-100, 1, 10, 100, 1000, 10000, 100000]

S = []
F = [0]*N
depth = [0]*N

# PreOrder(先行順巡回) 0 -> 1と追うやつ。典型。
from collections import deque
q = []
path = []
pathdepth = []
vertexCost1 = []
vertexCost2 = []
edgeCost1 = []
edgeCost2 = []

rootnode = 1
depth = [-1] * N
nodein = [-1] * N
nodeout = [-1] * N
q.append([rootnode, 0, 0, vertexCost[rootnode]])
curtime = -1
usedPreorder = [False] * N
preorder = []
postordercnt = [-1] * N
postorder = []
parent = [None] * N

# q: nodenum, depth, vcost
while len(q) != 0:
    curtime += 1
    curnode, curdepth, vcost, ecost = q.pop()
    if curnode >= 0: # 行き掛け
        if nodein[curnode] == -1:
            nodein[curnode] = curtime
        depth[curnode] = curdepth
        pathdepth.append(curdepth)
        path.append(curnode)
        edgeCost1.append(vcost)
        edgeCost2.append(vcost)
        vertexCost1.append(ecost)
        vertexCost2.append(ecost)
        if len(G[curnode]) == 0: # 子がいないときの処理
            nodeout[curnode] = curtime + 1
        for nextnode, nextvcost in G[curnode][::-1]:
            print("! ", nextnode, vcost)
            if depth[nextnode] != -1:
                continue
            q.append([~curnode, curdepth, nextvcost, -vertexCost[nextnode]])
            q.append([nextnode, curdepth + 1, nextvcost, vertexCost[nextnode]])
            parent[nextnode] = curnode
    else: # もどりがけ
        curnode = ~curnode
        if nodein[curnode] == -1:
            nodein[curnode] = curtime
        path.append(curnode)
        edgeCost1.append(0)
        edgeCost2.append(-vcost)
        vertexCost1.append(0)
        vertexCost2.append(ecost)
        pathdepth.append(curdepth)
        nodeout[curnode] = curtime + 1

# last
path.append(-1)
pathdepth.append(-1)
vertexCost1.append(0)
vertexCost2.append(-vertexCost[rootnode])
edgeCost1.append(0)
edgeCost2.append(0)

print("Parent:", parent)
print("Nodein:", nodein)
print("Nodeout:", nodeout)
print("Path:", path)
print("Depth", pathdepth)
print("vcost1", vertexCost1)
print("vcost2", vertexCost2)
print("ecost1", edgeCost1)
print("ecost2", edgeCost2)
#######
# 試験なので、疑似RMQ(実際はseg treeなど組む)
def rmq(a, l, r):
    resind = -1
    resval = 2**64
    for i in range(l, r):
        if a[i] < resval:
            resval = a[i]
            resind = i
    return resind

def rsq(a, l, r):
    return sum(a[l:r])

def lca(x, y):
    l = min(nodein[x], nodein[y])
    r = max(nodeout[x], nodeout[y])
    ind = rmq(pathdepth, l, r)
    return path[ind]

def subtreeVertexCost(x):
    l = nodein[x]
    r = nodeout[x]
    return rsq(vertexCost1, l, r)

def subtreeEdgeCost(x):
    l = nodein[x]
    r = nodeout[x]
    return rsq(edgeCost1, l + 1, r)

def pathQueryFromRootVertexCost(x):
    return rsq(vertexCost2, 0, nodein[x] + 1)
def pathQueryFromRootEdgeCost(x):
    return rsq(edgeCost2, 0, nodein[x] + 1)

def pathQueryVertexCost(x, y):
    a = lca(x,y)
    return pathQueryFromRootVertexCost(x) + pathQueryFromRootVertexCost(y) - 2 * pathQueryFromRootVertexCost(a) + vertexCost[a]
def pathQueryEdgeCost(x, y):
    a = lca(x,y)
    return pathQueryFromRootEdgeCost(x) + pathQueryFromRootEdgeCost(y) - 2 * pathQueryFromRootEdgeCost(a)



# LCA(4, 5) = 2
print(lca(4, 5))
# LCA(2, 4) = 2
print(lca(2, 4))

# subtreeEdgeCost(1)=111111
print(subtreeVertexCost(1))
# subtreeVCost(1)=31
print(subtreeEdgeCost(1))

# subtreeEdgeCost(2)=11110
print(subtreeVertexCost(2))
# subtreeVCost(2)=14
print(subtreeEdgeCost(2))

# subtreeEdgeCost(4)=1000
print(subtreeVertexCost(4))
# subtreeVCost(4)=0
print(subtreeEdgeCost(4))


print(pathQueryFromRootVertexCost(5))
print(pathQueryFromRootEdgeCost(5))

print(pathQueryFromRootVertexCost(6)) # 100001
print(pathQueryFromRootEdgeCost(6)) # 16

print(pathQueryVertexCost(3,5)) # 10110
print(pathQueryEdgeCost(3,5)) # 10

print(pathQueryVertexCost(2, 2)) # 10
print(pathQueryEdgeCost(2 ,2 )) # 0

print(pathQueryVertexCost(4,6)) # 101111
print(pathQueryEdgeCost(4,6)) # 23
