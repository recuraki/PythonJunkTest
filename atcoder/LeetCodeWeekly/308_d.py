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



from collections import deque
class topologicalSort():
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.edgeNum = [0] * n
    def makeEdge(self, u, v):
        assert u != v
        self.g[u].append(v)
        self.edgeNum[v] += 1 # 入次++
    def solve(self):
        q = deque([])
        ans = []
        for i in range(self.n):
            if(self.edgeNum[i] != 0): continue
            q.appendleft(i)
            ans.append(i)
        while(len(q) > 0):
            cur = q.popleft()
            for nxt in self.g[cur]:
                self.edgeNum[nxt] -= 1
                if self.edgeNum[nxt] == 0:
                    ans.append(nxt)
                    q.append(nxt)
        return ans


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        for i in range(len(rowConditions)):
            rowConditions[i][0] -= 1
            rowConditions[i][1] -= 1
        for i in range(len(colConditions)):
            colConditions[i][0] -= 1
            colConditions[i][1] -= 1
        def f(cond):
            g = [[] for _ in range(k)]
            ts = topologicalSort(k)
            uf = UnionFindAtCoder(k)
            for a,b in cond:
                #if uf.isSameGroup(a,b): return None
                #uf.Unite(a, b)
                g[a].append(b)
                ts.makeEdge(a, b)

            ans = ts.solve()
            se = set(ans)
            for i in range(k):
                if i not in se: ans.append(i)
            return ans

        r = f(rowConditions)
        c = f(colConditions)
        ans = [[0] * k for _ in range(k)]
        kind = [[None, None] for _ in range(k)]
        for i in range(k):
            x = r[i]
            kind[x][0] = i
        for i in range(k):
            x = c[i]
            kind[x][1] = i
        for i in range(k):
            h, w = kind[i]
            ans[h][w] = i + 1
        for a,b in rowConditions:
            if kind[a][0] > kind[b][0]:
                return []
        for a,b in colConditions:
            if kind[a][1] > kind[b][1]:
                return []
        return ans


st = Solution()

print(st.buildMatrix(k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]])==[[3,0,0],[0,0,1],[0,2,0]])
print(st.buildMatrix(k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]])==[])
print(st.buildMatrix(k = 3, rowConditions = [], colConditions = [])==[])
print(st.buildMatrix(8, [[1,2],[7,3],[4,3],[5,8],[7,8],[8,2],[5,8],[3,2],[1,3],[7,6],[4,3],[7,4],[4,8],[7,3],[7,5]] , [[5,7],[2,7],[4,3],[6,7],[4,3],[2,3],[6,2]])!= [])

