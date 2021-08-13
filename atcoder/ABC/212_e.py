import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        mod = 998244353
        n, m, k = map(int, input().split())
        dp = [0] * n
        g = [[] for _ in range(n)]
        for i in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)
        for i in range(n):
            g[i].append(i)
        dp[0] = 1
        for step in range(1, k + 1):
            newdp = [0] * n
            total = sum(dp) # 前の全ての歩数
            total %= mod
            for i in range(n):
                subtotal = total
                for brokenNode in g[i]:
                    #print("BN", brokenNode, dp[step-1][brokenNode])
                    subtotal -= dp[brokenNode]
                subtotal %= mod
                newdp[i] = subtotal
            dp = newdp
        print(dp[0])

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
        input = """3 1 4
2 3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 3
1 2
1 3
2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 3 100
1 2
4 5
2 3"""
        output = """428417047"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()