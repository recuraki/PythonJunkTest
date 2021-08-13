import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    dat = [a,b,c]
    dat.sort()
    if dat[1]-dat[0] == dat[2] - dat[1]:
        print("Yes")
    else:
        print("No")

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
        input = """5 1 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 4 3"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 5 5"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()