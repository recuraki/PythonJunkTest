import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = [0] * n
        for i in range(n):
            res[dat[i] - 1] = i+1
        print(" ".join(list(map(str, res))))
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
        input = """3
2 3 1"""
        output = """3 1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 2 3"""
        output = """1 2 3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
5 3 2 4 1"""
        output = """5 3 2 4 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()