import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, m = map(int, input().split())
        g = [[] for _ in range(n)]
        rg = [[] for _ in range(n)]
        cnt = [0] * n
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            rg[v].append(u)
            cnt[u] += 1
        from collections import deque
        q = deque([])
        for i in range(n):
            if cnt[i] == 0: q.append(i)
        ans = n
        while len(q) > 0:
            cur = q.popleft()
            ans -= 1
            for nn in rg[cur]:
                cnt[nn] -= 1
                if cnt[nn] == 0:
                    q.append(nn)
        print(ans)






    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """5 5
1 2
2 3
3 4
4 2
4 5"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2
1 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()