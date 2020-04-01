import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x, y, a, b, c = map(int,input().split())
    datp = sorted(list(map(int, input().split())), reverse=True)
    datq = sorted(list(map(int, input().split())), reverse=True)
    datr = list(map(int, input().split()))
    dat = sorted(datp[:x] + datq[:y] + datr, reverse=True)
    print(sum(dat[:x+y]))


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
        input = """1 2 2 2 1
2 4
5 1
3"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 2 2 2 2
8 6
9 1
2 1"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2 4 4 4
11 12 13 14
21 22 23 24
1 2 3 4"""
        output = """74"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2 2 4 4 8
11 12 13 14
21 22 23 24
100 100 100 100 100 100 100 100 100 """
        output = """400"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()