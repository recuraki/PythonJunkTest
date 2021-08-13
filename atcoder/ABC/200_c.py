import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def sigma1(n):
        return n * (n + 1) // 2

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = [0] * 200
        for x in dat:
            val = x %200
            buf[val] += 1
        res = 0
        for i in range(200):
            res += sigma1(buf[i]-1)
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
        input = """6
123 223 123 523 200 2000"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2 3 4 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
199 100 200 400 300 500 600 200"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()