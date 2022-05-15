import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')
    from decimal import Decimal
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        #from fractions import Fraction
        n, k = map(int, input().split())
        if k == 1:
            print("Infinity")
            return
        dat = []

        for _ in range(n):
            x, y = map(int, input().split())
            dat.append( (x, y) )
        dat.sort()
        from collections import defaultdict
        samelinex = defaultdict(int)
        sameliney = defaultdict(int)
        sameline = defaultdict(lambda : defaultdict(int))

        for i in range(n):
            x, y = dat[i]
            #print(x, y, "samelinex", x, samelinex)
            if samelinex[x] != 0: continue
            samelinex[x] += 1
            for j in range(i+1, n):
                xx, yy = dat[j]
                if x == xx: samelinex[x] += 1
            #print(x, y, "samelinex", x, samelinex)

        for i in range(n):
            x, y = dat[i]
            if sameliney[y] != 0: continue
            sameliney[y] += 1
            for j in range(i+1, n):
                xx, yy = dat[j]
                if y == yy: sameliney[y] += 1

        for i in range(n):
            ox, oy = dat[i]
            tmp = defaultdict(int)
            for j in range(i+1, n):
                x, y = ox, oy
                xx, yy = dat[j]
                if x == xx: continue
                if y == yy: continue
                if x > xx: # x < xxにしたい
                    x, xx = xx, x
                    y, yy = yy, y
                #katamuki = Fraction( yy-y, xx-x)
                katamuki = Decimal(yy - y) / Decimal(xx - x)
                tmp[katamuki] += 1

            x, y = ox, oy
            for katamuki in tmp.keys():
                genteny = y - (katamuki * x)
                if genteny in sameline[katamuki]: continue
                sameline[katamuki][genteny] = tmp[katamuki] + 1

        ans = 0
        #print(samelinex)
        #print(sameliney)
        for key in samelinex.keys():
            if samelinex[key] >= k:
                ans += 1
            #print("x", samelinex[key])
        for key in sameliney.keys():
            if sameliney[key] >= k:
                ans += 1
            #print("y", sameliney[key])
        for katamuki in sameline.keys():
            for genteny in sameline[katamuki].keys():
                if sameline[katamuki][genteny] >= k:
                    ans += 1
                    #print("HIT")
                #print(katamuki, genteny, sameline[katamuki][genteny])
        print(ans)

    do()


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
        input = """5 2
0 0
1 0
0 1
-1 0
0 -1"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
0 0"""
        output = """Infinity"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()