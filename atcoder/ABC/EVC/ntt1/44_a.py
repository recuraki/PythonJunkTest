import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())
    sum = 0
    for i in range(1, n + 1):
        if i <= (k):
            sum += x
        else:
            sum += y
    print(sum)

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
        logging.info("test_input_1")
        input = """5
3
10000
9000"""
        output = """48000"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """2
3
10000
9000"""
        output = """20000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()