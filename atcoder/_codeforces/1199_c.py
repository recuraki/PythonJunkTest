import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,i = map(int, input().split())
    dat = list(map(int, input().split()))
    import collections
    total = len(dat)
    c = collections.Counter(dat)
    d = []
    for k in c:
        d.append((k, c[k]))
    d.sort(key=lambda x: x[0])
    print(d)

    import math
    maxnum = math.floor(2**(8*i/n))

    l = 0
    r = 0
    maxcount = -1
    maxcountl = -1
    maxcountr = -1
    count = d[0][1]
    print("max = {0}".format(maxnum))
    while l < (len(d) - 1) :
        r += 1
        if r >= len(d):
            break
        #print("r = {0}".format(r))
        count += d[r][1]
        # 最大数未満なら続けていい
        if (r-l) < maxnum:
            if maxcount < count:
                maxcount = count
                maxcountl = l
                maxcountr = r
                #print("write1 c={0}, l={1}, r{2}".format(maxcount, maxcountl, maxcountr))
            continue
        # 超えたらちょうどいいところまで削る
        while l != r and ((r-l) >= maxnum):
            #print("!!! c={0}, l={1}, r{2}".format(count, l, r))
            count -= d[l][1]
            l += 1
            #print("l = {0}".format(l))
        # 成立したとき
        if maxcount < count:
            if (r - l) < maxnum:
                maxcount = count
                maxcountl = l
                maxcountr = r
                #print("write2 c={0}, l={1}, r{2}".format(maxcount, maxcountl, maxcountr))

    #rint("c={0}, l={1}, r{2}".format(maxcount,maxcountl,maxcountr))
    print(total - maxcount)










class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """6 1
2 1 2 3 4 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 2
2 1 2 3 4 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """50 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50"""
        output = """42"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()