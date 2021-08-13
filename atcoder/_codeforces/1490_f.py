import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import itertools

    def countstrswithIndex(s):
        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]
        d = countstrs(s)
        r = []
        ind = 0
        for i in range(len(d)):
            r.append((d[i][0], d[i][1], ind))
            ind += d[i][1]
        return r

    def do():
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort()
        sdat = createSDAT(dat)
        C = countstrswithIndex(dat)
        print(C)
        if len(C) == 1:
            print(0)
            return
        for i in range(len(C) - 1):
            pass


    q = int(input())
    for _ in range(q):
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
        input = """4
6
1 3 2 1 4 2
4
100 100 4 100
8
1 2 3 3 3 2 6 6
4
1 1 1 1"""
        output = """2
1
2
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()