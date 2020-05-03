import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from collections import Counter
    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))

        c = Counter(dat)
        m = 0
        realmax = max(dat)

        f = True
        mode = 2
        maxval = -1

        for i in range(1, realmax+1):
            if i not in c:
                f = False
                break
            if c[i] == 2:
                maxval = i
                continue
            if c[i] != 1:
                f = False
                break

        if n != maxval + realmax or f is False:
            print("0")
        else:
            lmax  = dat[:maxval]
            rmax  = dat[-maxval:]
            lreal = dat[:realmax]
            rreal = dat[-realmax:]
            lmax.sort()
            rmax.sort()
            lreal.sort()
            rreal.sort()
            ansm = list(range(1, maxval + 1))
            ansr = list(range(1, realmax + 1))
            res = []
            if lmax == ansm and rreal == ansr:
                res.append("{0} {1}".format(maxval, realmax))
            if lreal == ansr and rmax == ansm:
                res.append("{0} {1}".format(realmax, maxval))
            if len(res) == 2:
                if res[0] == res[1]:
                    res = [res[0]]
            print(len(res))
            if len(res) > 0:
                print("\n".join(res))

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
        input = """9
5
1 4 3 2 1
6
2 4 1 3 2 1
4
2 1 1 3
4
1 3 3 1
12
2 1 3 4 5 6 7 8 9 1 10 2
3
1 1 1
7
1 2 3 5 4 3 2
5
100 100 200 400 500
7
1 2 3 4 5 6 2"""
        output = """2
1 4
4 1
1
4 2
0
0
1
2 10
0
0
0
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5
2 3 4 2 3"""
        output = """2
1 4
4 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()