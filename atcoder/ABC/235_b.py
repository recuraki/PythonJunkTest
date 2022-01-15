import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math
    INF = 1 << 63
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        cur = 0
        while cur != (n-1) and dat[cur] < dat[cur+1]:
            cur += 1
        print(dat[cur])



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
1 5 10 4 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
100 1000 100000"""
        output = """100000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
27 1828 1828 9242"""
        output = """1828"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_3")
        input = """2
11 10"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()