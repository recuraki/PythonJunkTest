import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    def Base_n_to_10(X, n):
        out = 0
        for i in range(1, len(str(X)) + 1):
            out += int(X[-i]) * (n ** (i - 1))
        return out  # int out
    k = int(input())
    a, b = input().split()
    a = Base_n_to_10(a, k)
    b = Base_n_to_10(b, k)
    print(a*b)



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
        input = """2
1011 10100"""
        output = """220"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
123 456"""
        output = """15642"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()