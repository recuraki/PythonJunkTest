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
    pass
    q = int(input())
    for qq in range(q):
        a, b = map(int, input().split())
        r = 0
        for i in range(1, 11):
            if b >= ( (10**i)-1 ):
                r = i
        print(r*a)




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
        input = """3
1 11
4 2
191 31415926"""
        output = """1
0
1337"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()