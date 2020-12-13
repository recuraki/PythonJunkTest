import heapq
from collections import deque

INF = 2000000000
numV = 6
numV += 1 # for 1 origin

visited = [False] * numV
cost = [INF] * numV # cost
parent = [-1] * numV # parent node

# スタートとゴールの設定
nodes = 1
nodeg = 6
cost[nodes] = 0

q = [(0, nodes)] # 初期ノード(cost 0)
heapq.heapify(q)

# 辺の準備
e = []
for i in range(numV):
    e.append([])

# append (nextnode, cost)
e[1].append((2, 1))
e[1].append((3, 5))
e[2].append((1, 1))
e[2].append((3, 1))
e[3].append((4, 2))
e[3].append((6, 4))
e[4].append((5, 5))
e[4].append((6, 1))
e[5].append((2, 2))
e[6].append((5, 2))

# ダイクストラ
while len(q) > 0:
    curcost, curnode = heapq.heappop(q)
    # curnode == nodegの場合、計算を打ち切っても良いが今回はそのまま
    for nextnode, edgecost in e[curnode]:
        nextcost = curcost + edgecost
        if nextcost < cost[nextnode]:
            cost[nextnode] = nextcost
            parent[nextnode] = curnode
            heapq.heappush(q,  (nextcost, nextnode))

route = deque([])
nextnode = nodeg
while nextnode != -1:
    route.appendleft(str(nextnode))
    nextnode = parent[nextnode]

print("mincost:", cost[nodeg])
print(" -> ".join(route))