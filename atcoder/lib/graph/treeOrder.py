# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_7_C&lang=jp
# のグラフを用いる
"""
PreOrder: 上から辿りたい時に使える。上からコストを落としたい時など。
PostOrder: 下から辿りたい時に使える。下からコストを集約したい時など。

   0
   |
 +-+--+
 1    4
|+|  |+-|
2 3  5  8
    |+|
    6 7

Path: [0, 1, 2, 1, 3, 1, 0, 4, 5, 6, 5, 7, 5, 4, 8, 4, 0]
Parent: [None, 0, 1, 1, 0, 4, 5, 5, 4]
Nodein: [0, 1, 2, 4, 7, 8, 9, 3, 6]
Nodeout: [16, 5, 2, 4, 15, 12, 9, 11, 14]
Preorder: [0, 1, 2, 3, 4, 5, 6, 7, 8]
Postorder: [2, 3, 1, 6, 7, 5, 8, 4, 0]
"""
import sys

sys.setrecursionlimit(100000)

N = 9
G =[None] * N
G[0] = [1,4]
G[1] = [2,3]
G[2] = []
G[3] = []
G[4] = [5,8]
G[5] = [6,7]
G[6] = []
G[7] = []
G[8] = []

S = []
F = [0]*N
depth = [0]*N
def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d+1)
        S.append(v)

print(S)
dfs(0, 0)
print(S)

# PreOrder(先行順巡回) 0 -> 1と追うやつ。典型。
from collections import deque
q = []
path = []
rootnode = 0
depth = [-1] * N
nodein = [-1] * N
nodeout = [-1] * N
q.append([rootnode, 0])
curtime = -1
usedPreorder = [False] * N
preorder = []
postordercnt = [-1] * N
postorder = []
parent = [None] * N
while len(q) != 0:
    curtime += 1
    curnode, curdepth = q.pop()
    if nodein[curnode] == -1:
        nodein[curnode] = curtime
    if curnode >= 0: # 行き掛け
        depth[curnode] = curdepth
        preorder.append(curnode)
        path.append(curnode)
        postordercnt[curnode] = len(G[curnode])
        if len(G[curnode]) == 0: # 子がいないときの処理
            nodeout[curnode] = curtime
            postorder.append(curnode)
        for nextnode in G[curnode][::-1]:
            if depth[nextnode] != -1: continue
            q.append([~curnode, curdepth + 1])
            q.append([nextnode, curdepth + 1])
            parent[nextnode] = curnode
    else: # もどりがけ
        curnode = ~curnode
        path.append(curnode)
        nodeout[curnode] = curtime
        postordercnt[curnode] -= 1
        if postordercnt[curnode] == 0:
            postorder.append(curnode)

print("Path:", path)
print("Parent:", parent)
print("Nodein:", nodein)
print("Nodeout:", nodeout)
print("Preorder:", preorder)
print("Postorder:", postorder)

#######