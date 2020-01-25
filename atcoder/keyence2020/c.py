import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k, s = map(int, input().split())
    dat = [999999999] * n

    for i in range(k):
        dat[i] = s

    dat = list(map(str, dat))
    print(" ".join(dat))


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
        input = """4 2 3"""
        output = """1 2 3 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 3 100"""
        output = """50 50 50 30 70"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()