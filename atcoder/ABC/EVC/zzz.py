

import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, x = map(int, input().split())
    pl = lambda x: a * x + b * len(str(x))
    l = 0
    h = 10**9
    lastok = 0
    while l <= h:
        mid = (l + h) // 2
        if pl(mid) <= x: # 買うことができるなら
            lastok = mid
            l = mid + 1 # 買えるのでそれ以上の数
        else: # 買えないなら
            h = mid - 1 # 買えないのでそれ以下の数をトライ
    print(lastok)





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
        input = """10 7 100"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1 100000000000"""
        output = """1000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_1")
        input = """1000000000 1000000000 100"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_2")
        input = """1234 56789 314159265"""
        output = """254309"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()