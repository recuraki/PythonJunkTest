import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    s = input()
    ll = len(s)
    dat = list(map(int, list(s)))
    dp = collections.defaultdict(int)
    res = 0
    for r in range(ll):
        v = dat[r]
        ndp = collections.defaultdict(int)
        for k in dp.keys():
            nt = (k * 10 + v) % 2019
            ndp[nt] += dp[k]
        res += dp[0]
        ndp[v] += 1
        dp = ndp
    res += dp[0]
    print(res)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.maxDiff = 1000000
        self.assertEqual(out, output)
    def test_input_1(self):
        print("test_input_1")
        input = """1817181712114"""
        output = """3"""
        self.maxDiff = 1000000
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """14282668646"""
        output = """2"""
        self.maxDiff = 1000000
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()