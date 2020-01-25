import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    import collections
    sys.setrecursionlimit(1000000)
    n, q = map(int, input().split())
    cost = collections.deque([])
    tree = collections.deque([])
    level = collections.deque([])
    parent = collections.deque([])

    for i in range(210000):
        tree.append(collections.deque([]))
    level = collections.deque([-1] * 200100)
    parent = collections.deque([-1] * 200100)
    cost = collections.deque([0] * 200100)

    for loop in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    for loop in range(q):
        p, x = map(int, input().split())
        cost[p] += x

    def make_level(index, lev, pp):
        level[index] = lev
        parent[index] = pp
        for next in tree[index]:
            if level[next] != -1:
                continue
            cost[next] += cost[index]
            make_level(next, lev + 1, index)

    make_level(1, 0, -1)

    print(" ".join(list(map(str, cost))[1:n+1]))

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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()