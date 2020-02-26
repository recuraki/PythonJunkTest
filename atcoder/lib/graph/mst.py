"""
Prim法
始発点のcostを0としておく
全部の点の中から最もcostの低い未探索の点を探し、
その隣接の未探索の点をcostが既存より低ければminしていく
全ての点を探索するまで繰り返す
高速化していないのでO(N^2) 
"""
def ALDS1_12_A():
    n = int(input())
    primINF = 2000000000
    matrix = []
    numV = n
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    visited = [False] * numV
    cost = [primINF] * numV # cost
    parent = [-1] * numV # parent node

    cost[0] = 0
    parent[0] = -1

    while True:
        # 訪問済み隣接の最小コストのノードを探索する
        mincost = primINF
        for i in range(n):
            if visited[i] is False and cost[i] < mincost:
                mincost = cost[i]
                u = i
        # 見つからなければ終了する
        if mincost == primINF:
            break
        # 訪問済みにする
        visited[u] = True
        for v in range(n):
            if visited[v] is False and matrix[u][v] != -1:
                if matrix[u][v] < cost[v]:
                    cost[v] = matrix[u][v]
                    parent[v] = u
    res = 0
    for i in range(n):
        if parent[i] != -1:
            res += matrix[i][parent[i]]

    print(res)