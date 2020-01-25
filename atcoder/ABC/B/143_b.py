import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort(reverse=True)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += dat[i]*dat[j]
    print(res)

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
3 1 2"""
        output = """11"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
5 0 7 8 3 3 2"""
        output = """312"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()