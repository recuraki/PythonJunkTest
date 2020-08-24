import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h1, m1, h2, m2, k = map(int, input().split())
    if h1 == h2:
        print(m2 - m1 - k)
    else:
        x = 0
        x = 60 - m1
        x += m2
        x += 60 * (h2 - h1 - 1)
        print(x - k)



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
        input = """10 0 15 0 30"""
        output = """270"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 0 12 0 120"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """10 0 10 40 20"""
        output = """20"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """10 0 11 0 20"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()