import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x = map(int, input().split())
    dat_a = list(map(int, input().split()))
    s = bin(x)
    s = s[2:]
    res = 0
    for i in range(len(s)):
        if s[len(s)-1-i] == "1":
            res += dat_a[i]
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
    def test_input1(self):
        print("test_input1")
        input = """4 5
1 10 100 1000"""
        output = """101"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """20 1048575
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"""
        output = """210"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """4 0
1000 1000 1000 1000"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()