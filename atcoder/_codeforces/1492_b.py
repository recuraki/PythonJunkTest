import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        from heapq import heappop, heappush, heapify

        n = int(input())
        odat = list(map(int, input().split()))
        dat = []
        for i in range(n):
            dat.append((-odat[i], -i))
        heapify(dat)

        res = []

        totteru = n
        while len(dat) > 0:
            curVal, curInd = heappop(dat)
            curInd = -curInd
            if totteru <= curInd:
                continue
            for i in range(curInd, totteru):
                res.append(odat[i])
            totteru = curInd
        print(" ".join(list(map(str, res))))

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
4
1 2 3 4
5
1 5 2 4 3
6
4 2 5 3 6 1
1
1"""
        output = """4 3 2 1
5 2 4 3 1
6 1 5 3 4 2
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
2
1 2
"""
        output = """"""
        #self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()