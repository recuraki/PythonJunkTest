import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(taskno):
        n = int(input())
        dat = []
        total = 0
        for i in range(n):
            a,b = map(int, input().split())
            dat.append([a,b])
            total += a*b
        ototal = total
        dat.reverse()
        #print(dat, total)
        res = 0
        ss = set()
        ss.add((None, total))
        for i in range(n):
            xi, numi = dat[i]
            tmp = set()
            for sprod, psum in ss:
                for ii in range(1, numi + 1):
                    newprod = sprod * xi ** i if sprod is not None else xi ** i
                    psum = total - xi * i
                    if max(psum,newprod) > ototal:
                        continue
                    if newprod == psum:
                        res = max(res, newprod)
                    tmp.add((newprod, psum))
            ss = ss.union(tmp)
            print(ss)
        print("Case #{0}: {1}".format(taskno, res))
    q = int(input())
    for qq in range(q):
        do(qq+1)

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
5
2 2
3 1
5 2
7 1
11 1
1
17 2
2
2 2
3 1
1
2 7"""
        output = """Case #1: 25
Case #2: 17
Case #3: 0
Case #4: 8"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()