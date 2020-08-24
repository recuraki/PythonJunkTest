import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    Inf = 99999999999999
    n = int(input())
    s = input()
    dat1 = list(map(int, input().split()))
    dat2 = list(map(int, input().split()))
    dp = []
    for i in range(3100):
        dp.append([Inf] * 3100)
    dp[0][0] = 0
    for i in range(n):
        if s[i] == "(":
            for j in range(3100):
                if dp[i][j] == Inf:
                    continue
                # 削除 コストはdat2
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + dat2[i])
                # 何もしない(コストはかからない)
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j])
                # 変更 閉じるのでj==0のとき不可能
                if j > 0:
                    dp[i + 1][j-1] = min(dp[i + 1][j-1], dp[i][j] + dat1[i])
        if s[i] == ")":
            for j in range(3100):
                if dp[i][j] == Inf:
                    continue
                # 削除 コストはdat2
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + dat2[i])
                # 何もしない(コストはかからない)閉じるのでj==0のとき不可能
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                # 変更 "("
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + dat1[i])

    #for i in range(11):
    #    print(dp[i][:11])
    print(dp[n][0])

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
        input = """3
))(
3 5 7
2 6 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
(
10
20"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
))())((()(
13 18 17 3 20 20 6 14 14 2
20 1 19 5 2 19 2 19 9 4"""
        output = """18"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """4
()()
17 8 3 19
5 3 16 3"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()