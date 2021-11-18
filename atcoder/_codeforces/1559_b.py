import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():
    """
    同じ値のときだめ
    """

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        n = int(input())
        s = input()

        dp = [[-1] * 2 for _ in range(n)]
        route  = [[0] * 2 for _ in range(n)]

        # R = 0, B = 1
        if s[0] == "R" or s[0] == "?":
            dp[0][0] = 0
        if s[0] == "B" or s[0] == "?":
            dp[0][1] = 0
        for i in range(1, n):
            if s[i] == "R" or s[i] == "?":
                dp[i][0] = INF
                if dp[i-1][0] != -1:
                    if dp[i - 1][0] + 1 < dp[i][0]:
                        dp[i][0] =  dp[i - 1][0] + 1
                        route[i][0] = 0
                if dp[i-1][1] != -1:
                    if dp[i - 1][1] < dp[i][0]:
                        dp[i][0] = dp[i - 1][1]
                        route[i][0] = 1
            if s[i] == "B" or s[i] == "?":
                dp[i][1] = INF
                if dp[i-1][0] != -1:
                    if dp[i - 1][0] < dp[i][1]:
                        dp[i][1] =  dp[i - 1][0]
                        route[i][1] = 0
                if dp[i-1][1] != -1:
                    if dp[i - 1][1] + 1 < dp[i][1]:
                        dp[i][1] = dp[i - 1][1] + 1
                        route[i][1] = 1
        res = ""
        last = "a"
        if (dp[n-1][0] != -1) and (dp[n-1][0] <= dp[n-1][1] or dp[n-1][1] == -1): # last is 0(R)
            res += "R"
            last = 0
        else:
            res += "B"
            last = 1
        for i in range(n-1, 0, -1):
            next = route[i][last]
            if next == 0: res += "R"
            if next == 1: res += "B"
            last = next
        res = res[::-1]
        print(res)


    q = int(input())
    for _ in range(q):
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
        input = """5
7
?R???BR
7
???R???
1
?
1
B
10
?R??RB??B?"""
        output = """BRRBRBR
BRBRBRB
B
B
BRRBRBBRBR"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()