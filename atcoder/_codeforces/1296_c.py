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
        n = int(input())
        s = input()
        dat = dict()
        x, y,t = 0, 0,0
        dat[x*200000 + y] = 0
        l,r,d = -1,-1,99999999999
        #print("-----")
        for i in range(n):
            t += 1
            if s[i] == "L":
                x -= 1
            elif s[i] == "R":
                x += 1
            elif s[i] == "U":
                y += 1
            elif s[i] == "D":
                y -= 1
            #print("step t={0} x={1} y={2}".format(t, x, y))
            if (x * 200000 + y) in dat:
                cd = i - dat[x * 200000 + y]
                #print("visited! now = {2} prevtime ={0} cd = {1}".format(dat[x * 200000 + y], cd, t))
                if cd < d:
                    #print("short")
                    l = dat[x * 200000 + y]
                    r = t
                    d = cd
            dat[x * 200000 + y] = t
        if l == -1:
            print(-1)
        else:
            print("{0} {1}".format(l + 1,r))


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
4
LRUD
4
LURD
5
RRUDU
5
LLDDR"""
        output = """1 2
1 4
3 4
-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()