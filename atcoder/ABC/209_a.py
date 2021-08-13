import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    a,b = map(int, input().split())
    print(max(0, b-a+1))


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
        input = """2 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 100"""
        output = """91"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 2"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()