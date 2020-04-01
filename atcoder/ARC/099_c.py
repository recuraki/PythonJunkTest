import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n, k = map(int,input().split())
    dat = list(map(int, input().split()))

    i = dat.index(1) + 1 # 1 origin で i 個目に 1 がある

    reached = k # 最初の1歩はkマス塗れる
    # a: 残りはk-1マス塗れるので、残っている分を塗る(k<nなのでマイナスは考えない)
    a = math.ceil((n - reached) / (k - 1))
    print(1 + a)


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
        input = """4 3
2 3 1 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
1 2 3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 3
7 3 1 8 4 6 2 5"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()