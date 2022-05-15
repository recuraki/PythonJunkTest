import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n, x = map(int, input().split())
    s = list(input())
    depth = 0
    while x >= (2**depth):
        depth+= 1
    depth -= 1
    limit = 61
    for op in s:
        if op == "U":
            if depth <= limit: x //= 2
            depth -= 1
        elif op == "L":
            if (depth+1) <= limit: x = x*2 + 0
            depth += 1
        elif op == "R": # 右
            if (depth+1) <= limit:  x = x*2 + 1
            depth += 1
    print(x)




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
        input = """3 2
URL"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 500000000000000000
RRUU"""
        output = """500000000000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """30 123456789
LRULURLURLULULRURRLRULRRRUURRU"""
        output = """126419752371"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()