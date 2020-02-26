import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    res = [10000000] * n
    for i in range(0, n - 1):
        res[i] = min(dat[i], res[i])
        res[i+1] = min(dat[i], res[i+1])
    print(sum(res))

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
2 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
3"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
0 153 10 10 23"""
        output = """53"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()