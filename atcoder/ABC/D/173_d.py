import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort(reverse=True)
    res = dat[0]
    for i in range(0, n-2):
        x = i // 2
        res += dat[1+x]
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
        input = """4
2 2 1 3"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
1 1 1 1 1 1 1"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_22(self):
        print("test_input_2")
        input = """8
1 2 3 4 5 6 7 8"""
        output = """44"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()