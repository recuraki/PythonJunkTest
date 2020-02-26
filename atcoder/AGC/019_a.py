import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q, h, s, d = map(int,input().split())
    n = int(input())
    v1 = min(q*4, h*2, s* 1)
    v2 = min(v1 * 2, d)
    print(n // 2 * v2 + n%2 * v1)
    #print(v1, v2)

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
        input = """20 30 70 90
3"""
        output = """150"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10000 1000 100 10
1"""
        output = """100"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 100 1000 10000
1"""
        output = """40"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """12345678 87654321 12345678 87654321
123456789"""
        output = """1524157763907942"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()