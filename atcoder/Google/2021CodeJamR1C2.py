import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def resolve():
    from pprint import pprint
    def do(taskno):
        n = int(input())
        #if n < 10:
        #    print("Case #{0}: {1}".format(taskno, 12))
        #    return
        ns = str(n)
        candidate = []
        loopmax = len(ns) + 1
        #if n < 100:
        #    loopmax = 2
        for i in range(1, loopmax+2):
            #print(i)
            for offset in range(20):
                init = int(ns[:i]) + offset
                makestr = ""
                ii = 0
                while True:
                    makestr += str(init + ii)
                    if int(makestr) > n and ii != 0:
                        candidate.append((int(makestr),i,offset))
                        break
                    ii+= 1

        for kk in range(1,20):
            makestr = ""
            ii = 0
            while True:
                makestr += str(kk + ii)
                if int(makestr) > n and ii != 0:
                    candidate.append((int(makestr),i,offset))
                    break
                ii+= 1

        #pprint(candidate)
        candidate.sort()
        #pprint(candidate)
        for x in candidate:
            if x[0] > n:
                res = x[0]
                print("Case #{0}: {1}".format(taskno, res))
                return

    q = int(input())
    for qq in range(q):
        do(qq + 1)


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
2020
2021
68000
101"""
        output = """Case #1: 2021
Case #2: 2122
Case #3: 78910
Case #4: 123"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
9899099
"""
        output = """"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()