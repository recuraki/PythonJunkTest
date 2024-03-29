import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        n = int(input())
        def f(x):
            return (n - x) / n
        res = 0
        for i in range(0, n):
            tmp = f(i)
            res += 1 / tmp
        print(res - 1)
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
        input = """2"""
        output = """2.00000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3"""
        output = """4.50000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()