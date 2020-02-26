import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]
    q = int(input())
    for i in range(q):
        s = input()
        c = countstrs(s)
        #print(c)
        if c[0][0] == "0":
            del c[0]
        if len(c) > 0:
            if c[-1][0] == "0":
                del c[-1]
        res = 0
        for i in range(len(c)):
            if c[i][0] == "0":
                res += c[i][1]
        print(res)


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
        input = """1
0011001"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()