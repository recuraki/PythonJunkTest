def reroot(n, e):
    from collections import deque

    # ある頂点を根とした一番近い葉までの距離を計算する
    initCost = 999
    leafInitCost = 0
    op = min

    # ある頂点を根とした一番遠い葉までの距離を計算する
    initCost = 0
    leafInitCost = 0
    op = max

    dp = [initCost] * n
    parent = [-1] * n
    dfsRoute = deque([])


    # #####################これを入れていいかは問題による
    if n == 1:
        return [initCost]

    # DSFしていく。探索した順に記録。
    # 逆にたどることで確実にある頂点の部分木の下の方から訪問できる。
    root = 0
    q = deque([])
    q.appendleft([root, -1, initCost])
    while len(q) > 0:
        curNode, curparent, curCost = q.popleft()
        dfsRoute.append([curNode, curCost])
        for nextNode, cost in e[curNode]:
            if nextNode == curparent:
                continue
            parent[nextNode] = curNode
            q.appendleft([nextNode, curNode, cost])

    # route from parent
    #print("dfs route", dfsRoute)
    #print("parent llist", parent)

    # 逆に辿り、コストを計算していく。
    # ここで計算したいのは、ある頂点の部分木で最大のコスト
    for i in range(len(dfsRoute) - 1, -1, -1):
        curNode, curCost = dfsRoute[i]
        parNode = parent[curNode]
        if parNode == -1:
            continue
        # これが葉なら
        if len(e[curNode]) == 1:
            dp[curNode] = leafInitCost
        dp[parNode] = op(dp[parNode], dp[curNode] + curCost)

    # ここまででDFSの通常の木DPは終わり
    # 各頂点の部分木の最大コストがdp
    #print("dp", list(enumerate(dp)))

    # Rerootしていく。これは根からDSFしていく
    q = deque([])
    q.append([root, initCost])
    res = [initCost] * n
    while len(q) > 0:
        curNode, costFromParent = q.popleft()
        #print(">", curNode, costFromParent)
        #print("  dp", list(enumerate(dp)))
        #print("  res", list(enumerate(res)))
        parNode = parent[curNode]
        # childListはその頂点の部分木と根のコストの一覧
        childList = []
        # 今の頂点の隣接を探索していく。ここでのポイントは親側のコストの計算には、
        # queueで渡された値を使うこと。
        # そうしないと、親のコストは「自分を含む結果」を反射してしまう
        # つまり、その頂点 -> 親 -> その頂点を含む　
        for nextNode, nextCost in e[curNode]:
            if nextNode == parNode:
                childList.append([costFromParent + nextCost, nextNode])
                continue
            childList.append([dp[nextNode] + nextCost, nextNode])
        #childList.append([0, -1])

        # childListは探索順の値が入っている
        cl = len(childList)
        cumListFromL = [initCost] * cl
        cumListFromR = [initCost] * cl
        for i in range(cl - 1):
            cumListFromL[i+1] = op(cumListFromL[i], childList[i][0])
            cumListFromR[cl-1-1-i] = op(cumListFromR[cl-1-i], childList[cl-1-i][0])
        #print("!", childList)
        #print("!", cumListFromL)
        #print("!", cumListFromR)
        #print("  update", dp[curNode])
        res[curNode] = op(cumListFromL[cl-1], childList[cl-1][0])
        #print("  update", res[curNode])


        # 子の探索を行う
        for i in range(len(e[curNode])):
            nextNode, nextCost = e[curNode][i]
            # 親には戻らない
            if nextNode == parNode:
                continue
            q.append([nextNode, op(cumListFromL[i], cumListFromR[i])])
    return (res)

def GRL_5_A():
    n = int(input())
    e = []
    for _ in range(n):
        e.append([])
    # 両方への有向辺とする
    for _ in range(n-1):
        # node = 0 origin
        s,t,w = map(int, input().split())
        e[s].append([t, w])
        e[t].append([s, w])
    res = reroot(n, e)
    print(max(res))

def maxDistanceFromEachNode():
    n = 13
    e = []
    for _ in range(n):
        e.append([])
    # 両方への有向辺とする
    def adde(s,t,w):
        e[s].append([t, w])
        e[t].append([s, w])
    adde(0,1,1)
    adde(0,6,1)
    adde(1,2,100)
    adde(1,3,1)
    adde(3,4,50)
    adde(4,5,1)
    adde(6,7,1)
    adde(6,8,1)
    adde(8,9,1)
    adde(8, 10, 1)
    adde(10, 11, 1)
    adde(11, 12, 1)
    print(reroot(n, e))

maxDistanceFromEachNode()
#GRL_5_A()