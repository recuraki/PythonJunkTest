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

    n, q = map(int, input().split())
    u = UnionFindWithRank(n)
    for _ in range(q):
        c, a, b= map(int, input().split())
        a, b = a, b
        if c == 0:
            u.unite(a, b)
        else:
            print(1 if u.same(a, b) else 0)


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
        input = """5 12
0 1 4
0 2 3
1 1 2
1 3 4
1 1 4
1 3 2
0 1 3
1 2 4
1 3 0
0 0 4
1 0 2
1 3 0"""
        output = """0
0
1
1
1
0
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()