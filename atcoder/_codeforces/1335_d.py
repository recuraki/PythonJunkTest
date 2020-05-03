import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import collections
    import itertools

    q = int(input())
    for _ in range(q):
        dat = []
        for i in range(9):
            s = list(input().strip())
            dat.append(list(s))
        for ii in range(10):
            print("ii", ii)
            usednum = [False] * 10
            usedline = [False] * 10
            swapdat = []
            f = False
            for i in range(9):
                for tnc in range(1+ii, 1+9+ii): # try num
                    tn = tnc % 9 + 1
                    if usednum[tn]:
                        continue
                    ind = dat[i].index(str(tn))
                    if usedline[ind]:
                        continue
                    print("try num", tn, "line", i)
                    usednum[tn] = True
                    usedline[ind] = True
                    f = True
                    break
                if f is False:
                    break
            f = True
            for i in range(9):
                if usednum[i+1] is False:
                    f = False
            if f is True:
                break


        print(usednum)

        for i in range(9):
            print("".join(dat[i]))



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
        self.maxDiff= 999999
        print("test_input_1")
        input = """2
154873296
386592714
729641835
863725149
975314628
412968357
631457982
598236471
247189563
154873296
386592714
729641835
863725149
975314628
412968357
631457982
598236471
247189563"""
        output = """154873396
336592714
729645835
863725145
979314628
412958357
631457992
998236471
247789563"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()