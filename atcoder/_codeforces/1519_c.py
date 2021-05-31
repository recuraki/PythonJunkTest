import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import collections
    from collections import defaultdict
    import itertools
    def createSDAT(l):
        return list(itertools.accumulate(itertools.chain([0], l)))
    def do():
        n = int(input())
        datu = list(map(int, input().split()))
        dats = list(map(int, input().split()))
        members = defaultdict(list)
        for i in range(n):
            members[datu[i]].append(dats[i])
        res = [0] * n
        for k in members.keys():
            #print("k", k)
            l = members[k]
            l.sort(reverse=True)
            llen = len(l)
            sdat = createSDAT(l)
            squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
            for i in range(1, n + 1):
                #print(" loop", i)
                cangroup = llen // i
                canperson = cangroup * i
                #print("  > ", l[:canperson])
                res[i-1] += squery(0, canperson)


        print(" ".join(list(map(str, res))))

    q = int(input())
    for _ in range(q):
        do()
    # do()

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
        input = """1
7
1 2 1 2 1 2 1
6 8 3 1 5 1 5"""
        output = """29 28 26 19 0 0 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """4
7
1 2 1 2 1 2 1
6 8 3 1 5 1 5
10
1 1 1 2 2 2 2 3 3 3
3435 3014 2241 2233 2893 2102 2286 2175 1961 2567
6
3 3 3 3 3 3
5 9 6 7 9 7
1
1
3083"""
        output = """29 28 26 19 0 0 0
24907 20705 22805 9514 0 0 0 0 0 0
43 43 43 32 38 43
3083"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_11")
        input = """1
7
1 3 5 7 8 9 10
1 1 1 1 1 1 1
"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()