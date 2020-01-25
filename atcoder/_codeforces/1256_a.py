import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    qq = int(input())
    for q in range(qq):
        a, b, n, s = map(int, input().split())
        #print("{0}, {1}, {2}, {3}".format(a,b,n,s))
        x = s // n
        #print("x{0}".format(x))
        if x > a:
            x = a
        y = s - (x * n)
        #print("x:{0},  y:{1}".format(x,y))
        if y > b:
            print("NO")
        else:
            print("YES")


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
1 2 3 4
1 2 3 6
5 2 6 27
3 3 5 18"""
        output = """YES
NO
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


