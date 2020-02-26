import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, c = map(int, input().split())
    dat = [a,b,c]
    dat.sort()
    a,b,c = dat
    # cが一番長い
    #print(a,b,c)
    if a%2 == 0 or b%2 == 0 or c%2 == 0:
        print(0)
    else:
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
        input = """3 3 3"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2 4"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 3 5"""
        output = """15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()