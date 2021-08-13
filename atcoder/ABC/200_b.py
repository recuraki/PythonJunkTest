import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k =map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = int(str(n)+"200")
    print(n)

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
        input = """2021 4"""
        output = """50531"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """40000 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8691 20"""
        output = """84875488281"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()