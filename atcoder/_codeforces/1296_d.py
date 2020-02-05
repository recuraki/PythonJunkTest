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

    n, a, b, k = map(int,input().split())
    odat = list(map(int, input().split()))
    point = 0
    dat = []
    x = a + b
    #print("x={0}".format(x))
    for i in range(n):
        if odat[i] <= a:
            #print("{0} hp{1} is too yowai".format(i, odat[i]))
            point += 1
            continue
        if 0 < (odat[i] % x) <= a:
            #print("{0} hp{1} is my turn".format(i, odat[i]))
            point += 1
            continue
        sonota = odat[i] % x
        dat.append(x if sonota == 0 else sonota)
    #print("point")
    #print(point)
    #print("nokori")
    dat.sort()
    #print(dat)
    import math
    for i in range(len(dat)):
        #print("nokori k = {0}".format(k))
        if k <= 0:
            break
        needk = math.ceil(dat[i] / a) - 1
        #print("vs hp = {0} need k = {1}".format(dat[i],needk))
        if needk <= k:
            k -= needk
            point += 1
        else:
            break
    #print("point")
    print(point)




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
        input = """6 2 3 3
7 10 50 12 1 8"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1 100 99
100"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 4 2 1
1 3 5 4 2 7 6"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()