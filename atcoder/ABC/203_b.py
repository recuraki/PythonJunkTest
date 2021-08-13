import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    res = 0
    n, k = map(int, input().split())
    for i in range(n):
        for j in range(k):
            res += (i+1) * 100 + (j+1)
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
        input = """1 2"""
        output = """203"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3"""
        output = """1818"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()