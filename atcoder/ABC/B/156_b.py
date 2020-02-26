import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def Base_10_to_n(X, n):
        X_dumy = X
        out = ''
        while X_dumy > 0:
            out = str(X_dumy % n) + out
            X_dumy = int(X_dumy / n)
        return out

    n, k = map(int, input().split())
    print(len(str(Base_10_to_n(n, k))))

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
        input = """11 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1010101 10"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """314159265 3"""
        output = """18"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()