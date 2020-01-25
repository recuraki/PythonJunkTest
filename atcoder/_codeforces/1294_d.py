import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, xxx = map(int, input().split())
    dat = []
    for _ in range(n):
        dat.append(int(input()))

    import collections
    c = [0] * maxk

    isall = False
    curmax = -1
    datminin = -1
    isallm = 0
    datmin = 1000000008
    allcount = 0

    for qqq in range(n):
        mod = dat[qqq] % xxx

        c[mod] += 1

        if mod == isallm:
            while mod < xxx:
                if c[mod] <= allcount:
                    isallm = mod
                    break
                mod += 1
            if mod == xxx:
                allcount+= 1
                isallm = 0
                for i in range(xxx):
                    if c[i] <= (allcount):
                        isallm = i
                        break

        #print("xxx{0} allc{1} isallm{2} mod{3}".format(xxx, allcount, isallm, mod))
        print((xxx * allcount) + isallm)

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
        input = """7 3
0
1
2
2
0
0
10"""
        output = """1
2
3
3
4
4
7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1
2
1
2"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()