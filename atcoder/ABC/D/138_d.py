import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    sys.setrecursionlimit(1000000)
    n, q = map(int, input().split())
    res = []
    tree = []
    level = []
    childs = []
    parent = []
    for i in range(210000):
        res.append(0)
        tree.append([])
        level.append(-1)
        childs.append([])
        parent.append(-1)

    for loop in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    def make_level(index, lev):
        l = 0
        level[index] = lev
        for next in tree[index]:
            # 逆走はしない
            if level[next] != -1:
                continue
            # 子供に親を設定
            parent[next] = index
            curparent = index
            add_parent(index, next)
            make_level(next, lev + 1)

    def add_parent(index, childindex):
        if index != -1:
            childs[index].append((childindex))
            add_parent(parent[index], childindex)

    make_level(1, 0)

    for loop in range(q):
        p, x = map(int, input().split())
        res[p] += x
        for childindex in childs[p]:
            res[childindex] += x

    res = list(map(str, res))
    print(" ".join(res[1:n+1]))

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