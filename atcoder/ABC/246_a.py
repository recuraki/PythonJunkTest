
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        from collections import defaultdict
        datx = defaultdict(int)
        daty = defaultdict(int)
        x, y = map(int, input().split())
        datx[x] += 1
        daty[y] += 1

        x, y = map(int, input().split())
        datx[x] += 1
        daty[y] += 1

        x, y = map(int, input().split())
        datx[x] += 1
        daty[y] += 1

        for k in datx:
            if datx[k] == 1: ansx = k
        for k in daty:
            if daty[k] == 1: ansy = k
        print(ansx, ansy)


    # 1 time
    do()


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
        input = """-1 -1
-1 2
3 2"""
        output = """3 -1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-60 -40
-60 -80
-20 -80"""
        output = """-20 -40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()