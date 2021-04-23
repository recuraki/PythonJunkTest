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


class UnionFindDONTUSETooSlow(object):
    par = []

    def __init__(self, n):
        for i in range(n):
            self.par.append(i)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            p = self.root(self.par[x])
            self.par[x] = p
            return p

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        if self.same(x, y):
            return
        self.par[x] = y


class UnionFindWithRank(object):
    par = []
    rank = []
    cache = True
    log = []

    def __init__(self, n):
        for i in range(n):
            self.par.append(i)
            self.rank.append(0)

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            p = self.root(self.par[x])
            self.par[x] = p
            return p

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        ox, oy = x, y
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            x, y = y, x
            self.par[y] = x
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

        self.mathematica_dump("unite {0} and {1}".format(oy, ox))

    def mathematica_dump(self, action):
        t = []
        for i in range(len(self.par)):
            t.append("{0} -> {1}".format(str(i), str(u.par[i])))
        self.log.append ("{{" + ",".join(t) + '},"' + action + '"}')

def arc111_b():
    lma = 400000
    n = int(input())
    uf = UnionFindAtCoder(lma + 10)
    count = [0] * (lma + 10)
    dat = []
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        count[a] += 1
        count[b] += 1
        uf.Unite(a, b)
        dat.append((a, b))
    rcount = [0] * (lma + 10)
    for a, b in dat:
        rcount[uf.Find_Root(a)] += 1
    res = 0
    for i in range(lma):
        if uf.Find_Root(i) == i:
            if uf.size(i) == rcount[i] + 1:
                res += uf.size(i) - 1
            else:
                res += uf.size(i)
    print(res)


if __name__ == "__main__":
    u = UnionFindAtCoder(10)
    res = []
    u.Unite(0,1)
    u.Unite(1,2)
    u.Unite(3,4)
    u.Unite(4,5)
    u.Unite(2,3)
    u.Unite(9,8)
    u.Unite(9,8)
    u.Unite(3,8)
    u.Unite(6,3)
    print(u.all_group_members())
    print(u.size(10))
    #print('gs = {' + ",".join(u.log) +'}')
    #print('Manipulate[TreePlot[gs[[a]][[1]],  VertexLabels -> Automatic, PlotLabel -> gs[[a]][[2]]], {a, 1, ' + str(len(u.log)) + ' , 1}]')
