import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint
    import sys
    import math
    iinf = -(10**18)
    n, m, k = map(int, input().split())
    maxselect = m // 2
    maze = []
    for i in range(n):
        l = list(map(int, input().split()))
        maze.append(l)
    dp2 = []
    for hh in range(n):
        # init dp
        dp = []
        for i in range(m + 10):
            l = [None] * (k )
            dp.append(l)
        dp[0][0] = 0

        # each row
        for ww in range(m):
            v = maze[hh][ww]
            for i in range(maxselect, 0, -1): # select num (new)
                for j in range(k):
                    newj = (j + v) % k
                    oldjnum = dp[i-1][j]
                    if oldjnum is None:
                        continue
                    if dp[i][newj] is None:
                        dp[i][newj] = iinf
                    dp[i][newj] = max(dp[i][newj], oldjnum + v)
        l = [iinf] * k
        for i in range(k):
            for j in range(len(dp)):
                if dp[j][i] is None:
                    dp[j][i] = iinf
                l[i] = max(l[i], dp[j][i])
        #print(l)
        dp2.append(l)
    #pprint(dp2)
    res = []
    for i in range(n+1):
        l = [None] * k
        res.append(l)
    res[0][0] = 0
    from copy import deepcopy
    for i in range(0, n):
        for orij in range(k):  # original
            if res[i][orij] is None:
                continue
            for newj in range(k):
                newjj = (newj + orij) % k
                if res[i+1][newjj] is None:
                    res[i+1][newjj] = iinf
                res[i+1][newjj] = max(res[i+1][newjj], res[i][orij] + dp2[i][newj])
    print(res[n][0])









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
        input = """4 2 49
16 42
58 37
2 17
40 61"""
        output = """98"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()