import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n, h, l, r = map(int, input().split())
    data = list(map(int, input().split()))
    dp = [[-1] * h for i in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        x = data[i]
        for j in range(h):
            if dp[i][j] == -1: # not visit
                continue
            dp[i+1][(j + x    ) % h] = max(dp[i][j], dp[i+1][(j + x    ) % h] )
            dp[i+1][(j + x - 1) % h] = max(dp[i][j], dp[i+1][(j + x - 1) % h])
        x = 0
        for j in range(h):
            if dp[i+1][j] == -1: # not visit
                continue
            if l <= (j + x    ) % h <= r:
                dp[i+1][(j + x  ) % h] += 1
    print(max(dp[n]))



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
        input = """7 24 21 23
16 17 14 20 20 11 22"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()