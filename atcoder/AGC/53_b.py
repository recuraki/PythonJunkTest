import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 累積和
    import itertools
    # 注意: あくまで、bは開区間
    squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
    def createSDAT(l):
        return list(itertools.accumulate(itertools.chain([0], l)))
    res = 0
    n = int(input())
    dat = list(map(int, input().split()))
    total = sum(dat)
    sdat = createSDAT(dat)
    print(total)
    for ll in range(0, n+1):
        nokorill = n - ll
        print("ll,noko", ll, nokorill)
        for l in range(2*n - nokorill + 1):
            for r in range(l + ll, 2*n - nokorill):
                print("sq", l, l + ll, "sq",r, r + nokorill)
                t = total - squery(l, l + ll) - squery(r, r + nokorill)
                print(t)
                res = max(res, t)
    print(res)

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
1 2 3 4 5 6"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 4 5 8 7 6 3 2"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()