import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 998244353
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = 0
        dat.sort(reverse=False)
        #print(dat)
        res = 0
        buffer = 0
        for i in range(1, n):
            pval = dat[i-1]
            cval = dat[i]
            buffer *= 2
            buffer += pval * 1
            buffer %= mod
            res += cval * buffer
            res %= mod
        for i in range(0, n):
            res += dat[i] ** 2
        res %= mod
        print(res)

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
        input = """3
2 4 3"""
        output = """63"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
10"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
853983 14095 543053 143209 4324 524361 45154"""
        output = """206521341"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()