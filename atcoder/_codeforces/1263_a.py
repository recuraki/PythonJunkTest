import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    import math
    for qq in range(q):
        res = 0
        dat = list(map(int, input().split()))
        dat.sort()
        diff = dat[2] - dat[1]
        #print("diff:{0}".format(diff))
        if dat[0] <= diff:
            res += dat[0]
            dat[0] = 0
        else:
            res += diff
            dat[0] -= diff

        #print("res= {1} dat:{0}".format(dat, res))

        res += dat[0]
        dat[1] -= math.ceil(dat[0] / 2)
        #print("dat:{0}".format(dat))

        res += dat[1]
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
        input = """6
1 1 1
1 2 1
4 1 1
7 4 10
8 1 4
8 2 8"""
        output = """1
2
2
10
5
9"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()

