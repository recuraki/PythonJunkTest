
from collections import deque
# a-zに正方向と逆辺を張る
def addEdge(g, a, z):
    g[0][a].append(z)
    g[1][z].append(a)

# グラフの初期化
def initGraph(g, edgenum):
    g.append([]) # [0] 正方向のグラフ
    g.append([]) # [1] 逆方向のグラフ
    for _ in range(edgenum):
        g[0].append(deque(list()))
    for _ in range(edgenum):
        g[1].append(deque(list()))


def dfs(g, v, visited, vs):
    # 正方向のDFS
    visited[v] = True
    for i in range(len(g[0][v])):
        if visited[g[0][v][i]] is False:
            dfs(g, g[0][v][i], visited, vs)
    vs.append(v)


def rdfs(g, v, visited,  cmp, k):
    # 逆方向のDFS
    # kがcall元に指定される連結成分の通し番号
    visited[v] = True
    cmp[v] = k
    # 指定したノードの逆辺をたどる
    for i in range(len(g[1][v])):
        #print("go? {0}".format(g[1][v][i]))
        # 逆辺の先がrDFSで到達できないときのみ
        if visited[g[1][v][i]] is False:
            #print("yes")
            rdfs(g, g[1][v][i], visited,  cmp, k)

def scc(g, cmp):
    vs = []  # 帰りがけのリスト
    visited = [False] * len(g[0])
    cmp.extend([None] * len(g[0]))
    for i in range(len(g[0])):
        if visited[i] is False:
            dfs(g, i, visited, vs)

    visited = [False] * len(g[1])
    k = 0
    #pprint(vs)
    for i in range(len(vs) -1, -1, -1):
        #print("vited: i={0} vs[i] = {1}".format(i, vs[i]))
        #print(visited)
        if visited[vs[i]] is False:
            #print("rdfs [{0}]".format(i))
            rdfs(g, vs[i], visited, cmp, k)
            k += 1
    #pprint(vs)
    return k

vCount = 13 # 超点数
g = [] # グラフ。[0] = 正方向のグラフ。 [1] = 逆方向のグラフ
v = [] # 辺
cmp = []

from pprint import pprint
initGraph(g, edgenum=vCount)
addEdge(g, 0,12)
addEdge(g, 12, 11)
addEdge(g, 11, 8)
addEdge(g, 11, 10)
addEdge(g, 10, 9)
addEdge(g, 9, 8)
addEdge(g, 9, 7)
addEdge(g, 8,10)
addEdge(g, 7,6)
addEdge(g, 6,5)
addEdge(g, 5,7)
addEdge(g, 6,3)
addEdge(g, 6,4)
addEdge(g, 4,3)
addEdge(g, 3,2)
addEdge(g, 2,3)
addEdge(g, 4,1)

# vs:  [5, 2, 3, 1, 4, 6, 7, 9, 10, 8, 11, 12, 0]
# cmp: [0, 6, 7, 7, 5, 4, 4, 4, 3, 3, 3, 2, 1]
scc(g, cmp)
print(cmp)