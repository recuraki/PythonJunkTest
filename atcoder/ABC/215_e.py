import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint

    INF = 1 << 63

    def do():
        mod = 998244353
        n = int(input())
        s = input()
        dat = []
        for x in s: dat.append(ord(x) - ord("A"))
        print(dat)
        buf = [[] for _ in range(10)]
        res = 0
        for i in range(n):
            mustch = dat[i] # 絶対にとる文字
            dp = [[0]*2 for _ in range(n)]




        print(total % mod)

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
        input = """4
BGBH"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBIEIJEIJIJCGCCFGIEBIHFCGFBFAEJIEJAJJHHEBBBJJJGJJJCCCBAAADCEHIIFEHHBGF"""
        output = """330219020"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()