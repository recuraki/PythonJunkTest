import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    #import sys
    #sys.setrecursionlimit(100000)
    def dp(s):
        if True:
            print(s)
    def dpp(s):
        if True:
            pprint(s)
    q = int(input())
    s = input()
    a,b = map(int, input().split())
    dat = list(map(int, input().split()))

    import math
    math.ceil(1.2)
    math.floor(1.2)
    round(1.2, 3)

    dat = [1, 2, 3]
    print(" ".join(list(map(str, dat))))

    pass



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
        input = """3 3 2
1 2
2 1
3 3
3 2"""
        output = """3
DRD"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4 3
3 4
3 1
3 3
5 3
1 3
1 4"""
        output = """9
DDLUUUURR"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()