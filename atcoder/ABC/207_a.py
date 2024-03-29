import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b,c = map(int, input().split())
    dat = [a,b,c]
    dat.sort()
    print(dat[1] + dat[2])

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
        input = """3 4 5"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 6 6"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """99 99 98"""
        output = """198"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()