import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
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

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    n, m, k =map(int, input().split())

    uf = UnionFindWithRank(n)
    uf = UnionFind(n)
    bd = dict()
    fd = dict()

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        fd[200000 * a + b] = True
        fd[200000 * b + a] = True
        uf.union(a, b)

    for i in range(k):
        c,d = map(int, input().split())
        c -= 1
        d -= 1
        bd[200000 * c + d] = True
        bd[200000 * d + c] = True

    res = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if (200000 * i + j) not in fd and (200000 * i + j) not in bd:
                if uf.same(i, j):
                    res[i] += 1
                    res[j] += 1
    print(" ".join(list(map(str, res))))
    print(uf.all_group_members())




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()