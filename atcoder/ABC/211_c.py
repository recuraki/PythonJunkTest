import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    INF = 1 << 63
    def do():
        mod = 10**9 + 7
        from collections import defaultdict
        d = defaultdict(int)
        s = input()
        for x in s:
            if   x == "c":   d[x] += 1
            elif x == "h": d[x] += d["c"]
            elif x == "o": d[x] += d["h"]
            elif x == "k": d[x] += d["o"]
            elif x == "u": d[x] += d["k"]
            elif x == "d": d[x] += d["u"]
            elif x == "a": d[x] += d["d"]
            elif x == "i": d[x] += d["a"]
            d[x] %= 10**9 + 7
        print(d["i"])

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
        input = """chchokudai"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """atcoderrr"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """chokudaichokudaichokudai"""
        output = """45"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()