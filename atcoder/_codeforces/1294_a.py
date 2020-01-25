import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)

    q = int(input())
    for _ in range(q):
        a, b, c,n  = map(int,input().split())
        t =  (a+b+c+n) // 3
        if (a+b+c+n) % 3 == 0:
            d = 0
            d += (t - a)
            d += (t - b)
            d += (t - c)

            #print(d)
            if (t-a) < 0 or (t-b) < 0 or (t-c) < 0:
                print("NO")
            elif d == n:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")



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
5 3 2 8
100 101 102 105
3 2 1 100000000
10 20 15 14
101 101 101 3
100000 0 0 2"""

        output = """YES
YES
NO
NO
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()