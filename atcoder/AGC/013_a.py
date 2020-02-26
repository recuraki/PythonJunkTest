import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    mode = 0 #  0: None, 1: add, 2: sub
    res = 1
    for i in range(1, n):
        if mode == 0:
            if dat[i-1] == dat[i]:
                mode = 0
            if dat[i-1] > dat[i]:
                mode = 2
            if dat[i-1] < dat[i]:
                mode = 1
        if mode == 1:
            if dat[i-1] == dat[i]:
                pass
            if dat[i-1] > dat[i]:
                res += 1
                mode = 0
            if dat[i-1] < dat[i]:
                pass
        if mode == 2:
            if dat[i-1] == dat[i]:
                pass
            if dat[i-1] > dat[i]:
                pass
            if dat[i-1] < dat[i]:
                res += 1
                mode = 0
    print(res)





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
        input = """6
1 2 3 2 2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9
1 2 1 2 1 2 1 2 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
1 2 3 2 1 999999999 1000000000"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()