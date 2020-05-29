import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    from decimal import Decimal
    for _ in range(q):
        h,c,t = map(int, input().split())
        h, c = h-t, c - t
        h = Decimal(h)
        c = Decimal(c)
        #print("---------",h,c)

        if h <= 0:
            print(1)
        elif c >= 0:
            print(2)
        else:
            isPrevMinus = True
            cnth = 0
            cntc = 0
            #print(h,c)
            minind = 0
            minval = Decimal(99999999999999)
            i = 0
            while i < minind + 10:
                i+=1
                if i % 2 == 1:
                    cnth += 1
                else:
                    cntc += 1
                t = ((cnth*h) + (cntc*c) ) / (cnth+cntc)
                #print(" i",i, cnth, cntc)
                #print(i, t)
                if t == 0:
                    minval = t
                    minind = i
                    #print("hit")
                    break

                if isPrevMinus and t < 0:
                    t = abs(t)
                    if t < minval:
                        minval = t
                        minind = i

                    #print("loopminus")
                    break
                if isPrevMinus is False and t > 0:
                    t = abs(t)
                    if t < minval:
                        minval = t
                        minind = i

                    #print("loopplus")
                    break
                if t < 0:
                    isPrevMinus = True
                else:
                    isPrevMinus = False

                t = abs(t)
                if t < minval:
                    minval = t
                    minind = i


            print(minind)





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
30 10 20
41 15 30
18 13 18"""
        output = """2
7
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()