from typing import List, Tuple
from pprint import pprint

# https://note.nkmk.me/python-union-find/
# https://qiita.com/Kerzival/items/6923c2eb3b91be86f19f
class UnionFindAtCoder():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1] * (n + 1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0] * (n + 1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if (self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if (x == y):
            return
            # 違う木に属していた場合rnkを見てくっつける方を決める
        elif (self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if (self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

    # Listing all nodes same as group of x
    # O(N)
    def members(self, x):
        root = self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i) == root]

    # List all root
    #O(N)
    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    # root Count
    def group_count(self):
        return len(self.roots())

    # {4: [0, 1, 2, 3, 4, 5, 6, 8, 9], 7: [7], 10: []}
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def size(self, x):
        return -self.root[self.Find_Root(x)]


from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        dsu = UnionFindAtCoder(n)
        g = defaultdict(list)
        costNode = defaultdict(list) # あるコストのノード
        ans = 0

        # 大きい方から小さい方への辺を貼る
        for i in range(n):
            costNode[vals[i]].append(i)
        # 大きいノードの時, 小さいノードに辺を貼る計算をする
        for u, v in edges:
            u, v = min(u, v), max(u, v) # u <= v
            if vals[u] > vals[v]: u, v = v, u
            g[v].append(u)
        # メイン処理
        leadercost = [0] * n
        for cost in range(100000 + 10):
            #if cost < 10:
            #    print(cost, ans)
            curcost = 0
            for curNode in costNode[cost]:
                leadercost[curNode] = 0
                for nextNode in g[curNode]: # curnode -> nextNodeで貼りたい
                    leadercost[nextNode] = 0

            # あるコストの処理を開始する costNode[cost]
            procLeader = set()
            for curNode in costNode[cost]:
                leadercost[dsu.Find_Root(curNode)] += 1
                curcost += 1
            for curNode in costNode[cost]:
                procLeader.add(dsu.Find_Root(curNode))
            for curNode in costNode[cost]:
                for nextNode in g[curNode]: # curnode -> nextNodeで貼りたい
                    if dsu.isSameGroup(curNode, nextNode): continue # 既に一緒なら何もしない
                    uCost = leadercost[dsu.Find_Root(curNode)]
                    vCost = leadercost[dsu.Find_Root(nextNode)]
                    newVal = uCost + vCost
                    curcost += uCost * vCost
                    dsu.Unite(curNode, nextNode)
                    leadercost[dsu.Find_Root(curNode)] = newVal
            ans += curcost
        return ans
