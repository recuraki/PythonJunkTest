import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque

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

            if x > y:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def same(self, x, y):
            return self.find(x) == self.find(y)

    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    cnt, edge = [0] * N, [set([]) for _ in range(N)]
    for _ in range(N - 1):
        A, B = map(int, input().split())
        if A == B:
            continue
        edge[A - 1].add(B - 1)
        edge[B - 1].add(A - 1)
        cnt[A - 1] += 1
        cnt[B - 1] += 1
    # print("cnt", cnt)
    # children = [[(X[i], i)] for i in range(N)]
    children = [[X[i]] for i in range(N)]
    uf = UnionFind(N)
    deq = deque([i for i, c in enumerate(cnt) if c == 1 and i != 0])
    parent = [-1] * N
    while deq:
        cur = deq.popleft()
        # print("cur", cur+1, "edge", edge[cur], "child", children[cur])
        while edge[cur]:
            nxt = edge[cur].pop()
            if nxt == parent[cur]: continue
            edge[nxt].discard(cur)
            if uf.same(cur, nxt) and nxt not in deq:
                continue
            uf.union(cur, nxt)
            children[nxt] += children[cur].copy()
            children[nxt].sort(reverse=True)
            children[nxt] = children[nxt][:20]
            # children[nxt] = list(set(children[nxt][:20]))
            # print("nxt", nxt+1, "child", children[nxt])
            if uf.find(nxt) == 0:
                continue
            parent[nxt] = cur
            deq.append(nxt)
    # print(children)
    ans = []
    for _ in range(Q):
        V, K = map(int, input().split())
        # ans.append(children[V-1][K-1][0])
        try:
            ans.append(children[V - 1][K - 1])
        except Exception:
            pass
    print(*ans, sep="\n")


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
        input = """5 2
1 2 3 4 5
1 4
2 1
2 5
3 2
1 2
2 1"""
        output = """4
5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 2
10 10 10 9 8 8
1 4
2 1
2 5
3 2
6 4
1 4
2 2"""
        output = """9
10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
1 10 100 1000
1 2
2 3
3 4
1 4
2 3
3 2
4 1"""
        output = """1
10
100
1000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()