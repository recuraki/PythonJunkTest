import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #input = sys.stdin.readline

    from pprint import pprint
    import sys

    q = int(input())
    for qq in range(q):
        n, m = map(int, input().split())
        data = []
        datb = []
        maxvala = -1
        maxvalb = -1
        maxind = -1
        for i in range(m):
            a,b = map(int, input().split())
            data.append(a)
            datb.append(b)
            if maxvalb > ma




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
        input = """2
4 3
5 0
1 4
2 2

5 3
5 2
4 2
3 1"""
        output = """14
16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()