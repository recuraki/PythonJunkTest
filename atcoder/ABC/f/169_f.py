import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, s = map(int, input().split())
    dat = list(map(int, input().split()))
    dat.sort()
    dp = []

    for i in range(n + 10):
        l = []
        for j in range(s+10):
            l.append([])
        dp.append(l)

    from pprint import pprint
    #pprint(dp)
    from copy import deepcopy

    resdat = []
    for j in range(n + 10):
        resdat.append([])

    for i in range(n):
        val = dat[i]
        if val > s: # sより大きいものは受け付けない（存在しないけども)
            continue
        for j in range(i+1, 0, -1): # j個選んだやつ
            for k in range(0, s-val+1): # そのj個目の値を 0 - 可能な数までスイープ
                dp[j+1][k+val].extend(dp[j][k])
                if k+val == s:
                    for x in dp[j+1][k+val]:
                        resdat[j+1].append( (x, i) )


        if dat[i] == s:
            resdat[1].append((i, i))
        elif dat[i] < s: # ただ一つの時用の書き込み
            dp[1][val].append(i)

    pprint(resdat)

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
        input = """3 4
2 2 4"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 8
9 9 9 9 9"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 10
3 1 4 1 5 9 2 6 5 3"""
        output = """3296"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """10 10
1 1 1 1 1 1 1 1 1 1"""
        output = """3296"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()