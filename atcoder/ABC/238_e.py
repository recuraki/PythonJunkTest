import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        n, que = map(int, input().split())
        g = [[] for _ in range((n + 1))]
        rg = [[] for _ in range((n + 1))]
        known = [False] * (n + 1)
        known[0] = True
        from collections import deque
        q = deque([1])
        for _ in range(que):
            a, b = map(int, input().split())
            g[a].append(b)
            rg[b].append(a)
        for i in range(n + 1):
            g[i].sort()
            rg[i].sort()
        while len(q) > 0:
            curnode = q.popleft()
            # print("cur!", curnode)
            for rnode in rg[curnode]:  # 逆辺をたどる
                if known[rnode - 1]: continue  # もう知っている方法ならどうでもいい
                # print("!r",nnode)
                q.appendleft(rnode)

            if not known[curnode - 1]: continue  # この辺はたどれない
            known[curnode] = True

            for nnode in g[curnode]:
                if known[nnode]: continue  # もう知っている方法ならどうでもいい
                known[nnode] = True
                # print("!n",nnode)
                q.append(nnode)
        # print(known)
        print("Yes" if known[n] else "No")

    do()


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
        input = """3 3
1 2
2 3
2 2"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 3
1 2
2 3"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 4
1 1
2 2
3 3
1 4"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()