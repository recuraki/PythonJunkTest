import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k = int(input())
    a, b = map(int, input().split())
    can = False
    for i in range(a, b+1):
        if i % k == 0:
            can = True
    print("OK" if can else "NG")

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
        input = """7
500 600"""
        output = """OK"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
5 7"""
        output = """NG"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1
11 11"""
        output = """OK"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()