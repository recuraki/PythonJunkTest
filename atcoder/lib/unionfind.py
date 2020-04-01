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

    def members(self, x):
        root = self.Find_Root(x)
        return [i for i in range(self.n) if self.Find_Root(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def size(self, x):
        return -self.root[self.Find_Root(x)]


class UnionFind(object):
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

if __name__ == "__main__":
    u = UnionFindWithRank(11)
    res = []
    u.unite(0,1)
    u.unite(1,2)
    u.unite(3,4)
    u.unite(4,5)
    u.unite(2,3)
    u.unite(9,10)
    u.unite(9,8)
    u.unite(3,8)
    u.unite(6,7)
    u.unite(6,3)
    u.root(8)
    u.root(10)
    print('gs = {' + ",".join(u.log) +'}')
    print('Manipulate[TreePlot[gs[[a]][[1]],  VertexLabels -> Automatic, PlotLabel -> gs[[a]][[2]]], {a, 1, ' + str(len(u.log)) + ' , 1}]')
