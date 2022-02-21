import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = [0, 360]
        cur = 0
        for x in dat:
            cur += x
            cur %= 360
            buf.append(cur)
        buf.sort()
        ans = []
        for i in range(len(buf) - 1):
            x = buf[i+1] - buf[i]
            ans.append(x)
        ans.sort(reverse=True)
        print(ans[0])


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
        input = """4
90 180 45 195"""
        output = """120"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
1"""
        output = """359"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
215 137 320 339 341 41 44 18 241 149"""
        output = """170"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()