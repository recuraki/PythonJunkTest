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
    for _ in range(q):
        s = input()
        l = countstrs(s)
        dat = []
        for i in range(len(l)):
            a,cnt = l[i]
            if a == "1":
                dat.append(cnt)
        dat.sort(reverse=True)
        res = 0
        for i in range(len(dat)):
            if i&1 == 0:
                res += dat[i]
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
        input = """5
01111001
0000
111111
101010101
011011110111"""
        output = """4
0
6
3
6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()