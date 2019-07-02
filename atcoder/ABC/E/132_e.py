import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())

    visited = [False] * (n + 1)
    link = []
    for i in range(n + 1):
        link.append([])

    dat = []
    for i in range(m):
        u, v = map(int, input().split())
        dat.append((u, v))
        link[u].append((v))


    s,t = map(int, input().split())
    visited[s] = True # スタートはもう来てる

    def hop(s, n):
        if n == 0:
            if visited[s] is not True:
                visited[s] = True
                return set([s])
            else:
                return set()

        res = set()
        for i in range(len(link[s])):
            res.update(hop(link[s][i], n - 1))
        return res

    import collections
    cur = collections.deque([])

    cur.append((s,0))
    hops = collections.deque([])
    while len(cur) != 0:
        x = cur.pop()
        next, hopcount = x[0], x[1]
        r = hop(next, 3)
        r = list(r)
        for i in range(len(r)):
            if r[i] == t:
                hops.append(hopcount + 1)
            cur.append( (r[i], hopcount + 1) )


    if len(hops) == 0:
        print(-1)
    else:
        print(min(hops))




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
        input = """4 4
1 2
2 3
3 4
4 1
1 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1 2
2 3
3 1
1 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 0
1 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6 8
1 2
2 3
3 4
4 5
5 1
1 4
1 5
4 6
1 6"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()