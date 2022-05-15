
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
        mod = 998244353
        n, m, k, s, t, target = map(int, input().split())

        s -= 1
        t -= 1
        target -= 1

        g = [[] for _ in range(n)]
        for i in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        dp[s][0][0] = 1
        for turn in range(0, k): # turn から turn+1への遷移を計算
            for node in range(n): # 全ノードをなめて
                for nn in g[node]:
                    if nn == target: # 対象の場合！
                        dp[nn][turn+1][0] += dp[node][turn][1]
                        dp[nn][turn+1][1] += dp[node][turn][0]
                    else:
                        dp[nn][turn+1][0] += dp[node][turn][0]
                        dp[nn][turn+1][1] += dp[node][turn][1]
                    dp[nn][turn+1][0] %= mod
                    dp[nn][turn+1][1] %= mod
        print(dp[t][k][0])

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
        input = """4 4 4 1 3 2
1 2
2 3
3 4
1 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5 10 1 2 3
2 3
2 4
4 6
3 6
1 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 15 20 4 4 6
2 6
2 7
5 7
4 5
2 4
3 7
1 7
1 4
2 9
5 10
1 3
7 8
7 9
1 6
1 2"""
        output = """952504739"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()