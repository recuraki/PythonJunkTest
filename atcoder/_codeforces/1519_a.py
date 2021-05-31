
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline


    from pprint import pprint
    import math
    def do():
        r,g,d = map(int, input().split())
        r, g = min(r,g), max(r,g)
        diff = math.ceil(g / r)
        if (diff - 1) > d:
            print("NO")
        else:
            print("YES")

    q = int(input())
    for _ in range(q):
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
1 1 0
2 7 3
6 1 4
5 4 0"""
        output = """YES
YES
NO
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()