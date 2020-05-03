import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    if n < 2:
        print(0)
    elif (n % 2)  == 0:
        print(n //2 - 1)
    else:
        print(n // 2)

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
        input = """4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """999999"""
        output = """499999"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_211(self):
        print("test_input_211")
        input = """3"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2111(self):
        print("test_input_2111")
        input = """2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_21111(self):
        print("test_input_21111")
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_21111(self):
        print("test_input_21111")
        input = """5"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_211111(self):
        print("test_input_211111")
        input = """6"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()