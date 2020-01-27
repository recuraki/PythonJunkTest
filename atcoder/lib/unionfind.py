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
