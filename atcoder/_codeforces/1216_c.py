import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    def do_mask(x1, y1, x2, y2, x3, y3, x4, y4):
        # print(x1, y1, x2, y2, x3, y3, x4, y4)
        if x1 == -1:
            return -1, -1, -1, -1
        # zenbu-kakusu
        if x3 <= x1 and x2 <= x4 and y3 <= y1 and y2 <= y4:
            return -1, -1, -1, -1

        # haba-kakusu
        if x3 <= x1 and x2 <= x4:
            if y3 <= y1 and y1 <= y4:
                y1 = y4
            if y3 <= y2 and y2 <= y4:
                y2 = y3

        # yoko-kakusu
        if y3 <= y1 and y2 <= y4:
            if x3 <= x1 and x1 <= x4:
                x1 = x4
            if x3 <= x2 and x2 <= x4:
                x2 = x3

        return x1, y1, x2, y2

    x1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x3, y3, x4, y4)
    x1, y1, x2, y2 = do_mask(x1, y1, x2, y2, x5, y5, x6, y6)
    print("NO" if x1 == -1 else "YES")




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
        input = """2 2 4 4
1 1 3 5
3 1 5 5"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 7 5
0 0 4 6
0 0 7 4"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 2 10 5
3 1 7 6
8 1 11 7"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """0 0 1000000 1000000
0 0 499999 1000000
500000 0 1000000 1000000"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()