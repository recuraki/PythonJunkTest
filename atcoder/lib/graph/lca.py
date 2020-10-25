import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    numv = int(input())
    rootnode = 0
    parentlist = [None] * numv
    distlist = [-1] * numv
    e = []
    for i in range(numv):
        e.append([])
    dt = []
    for i in range(63):
        l = [-1] * numv
        dt.append(l)

    # make edge
    for i in range(numv):
        dat = list(map(int, input().split()))
        for j in dat[1:]:
            e[i].append(j)
            e[j].append(i)

    # calc depth and parent node
    from collections import deque
    q = deque([])
    q.append([rootnode, -1, 0])
    while len(q) != 0:
        node, parent, d = q.popleft()
        parentlist[node] = parent
        distlist[node] = d
        for nextnode in e[node]:
            if parentlist[nextnode] is not None: # visited
                continue
            q.append([nextnode, node, d + 1])

    # doubling calc
    for i in range(numv):
        dt[0][i] = parentlist[i]
    for i in range(1,63):
        for curnode in range(numv):
            p1 = dt[i-1][curnode]
            p2 = dt[i-1][p1] if p1 != -1 else -1
            dt[i][curnode] = p2

    def ancestor(node, n):
        i = 0
        cur = node
        while n != 0:
            x = 2 ** i
            if (n & x) != 0: # this bit is 1
                n ^= x # this bit is off
                cur = dt[i][cur]
            i += 1
        return cur

    def lca(nodeu, nodev):
        if nodeu == nodev:
            return nodeu
        tu = nodeu
        tv = nodev
        for k in range(60, -1, -1):
            mu = ancestor(tu, 2**k)
            mv = ancestor(tv, 2**k)
            if mu != mv:
                tu = mu
                tv = mv
        assert ancestor(tu, 1) == ancestor(tv, 1)
        return ancestor(tu, 1)

    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        # u < v
        if distlist[u] > distlist[v]:
            u, v = v, u
        d = distlist[v] - distlist[u]
        v = ancestor(v, d)
        print(lca(u, v))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_2(self):
        print("test_input_2")
        input = """8
3 1 2 3
2 4 5
0
0
0
2 6 7
0
0
4
4 6
4 7
4 3
5 2"""
        output = """1
1
0
0"""
        self.assertIO(input, output)


    def test_input_1(self):
        print("test_input_1")
        input = """40
3 1 2 3
3 4 5 6
2 7 8
2 9 10
2 11 12
1 13
2 14 15
1 16
2 17 18
2 19 20
0
0
2 21 22
0
0
2 25 26
0
2 31 32
0
0
0
0
2 23 24
0
0
1 33
2 27 28
2 29 30
0
0
1 39
0
0
1 34
2 35 36
0
2 37 38
0
0
0
15
24 11
23 13
23 35
14 39
14 37
34 39
37 39
29 28
29 39
39 32
31 7
20 37
35 25
38 6
38 0
"""
        output = """4
1
1
6
6
15
15
26
27
0
2
0
25
6
0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()