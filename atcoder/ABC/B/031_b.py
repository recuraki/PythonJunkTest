import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    l, h = map(int, input().split())
    n = int(input())
    for i in range(n):
        a = int(input())
        if a > h:
            print("-1")
        elif a < l:
            print(l - a)
        else:
            print("0")

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
        input = """300 400
3
240
350
480"""
        output = """60
0
-1"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """50 80
5
10000
50
81
80
0"""
        output = """-1
0
-1
0
50"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()