import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import math
    q = int(input())
    for _ in range(q):
        a,b,c,d = map(int, input().split())
        #print("---",a,b,c,d)
        if b >= a:
            print(b)
            continue
        a -= b
        if d >= c:
            print(-1)
            continue
        percycle = c - d
        needcycle = math.ceil( a / percycle)
        print(b + (c * needcycle))




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
        input = """7
10 3 6 4
11 3 6 4
5 9 4 10
6 5 2 3
1 1 1 1
3947465 47342 338129 123123
234123843 13 361451236 361451000"""
        output = """27
27
9
-1
1
6471793
358578060125049"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()