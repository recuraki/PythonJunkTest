import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    qq = int(input())
    import itertools

    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]
    for _ in range(qq):
        s = input()
        d = countstrs(s)
        ma = 0
        for k in d:
            if k[0] == "L":
                ma = max(ma, k[1])
        print(ma+1)



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
LRLRRLL
L
LLR
RRRR
LLLLLL
R"""
        output = """3
2
3
1
7
1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()