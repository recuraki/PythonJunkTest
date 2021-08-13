import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    x, y, z = map(int,input().split())
    for i in range(1000000, -1, -1):
        if y/x > i/z:
            print(i)
            break


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
        input = """100 200 100"""
        output = """199"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """103 971 593"""
        output = """5590"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000 1 1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()