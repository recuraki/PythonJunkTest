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
    # 注意: あくまで、bは開区間

    def do():
        from copy import deepcopy
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))
        n = int(input())
        dat = list(map(int, input().split()))
        res = []
        odat = deepcopy(dat)

        dat.sort()
        sdat = createSDAT(dat)
        needMin = 0
        for i in range(n-1):
            canPower = squery(0, i+1)
            if canPower < dat[i + 1]:
                needMin = (i + 1)
        needVal = dat[needMin]

        for i in range(n):
            if odat[i] >= needVal:
                res.append(i + 1)


        #print("min ind", needMin, "=", dat[needMin])
        print(len(res))
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
        input = """2
4
1 2 4 3
5
1 1 1 1 1"""
        output = """3
2 3 4
5
1 2 3 4 5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
4
100 1 1 1
4
2 2 2 5
6
1 5 1 5 10 10
1
10"""
        output = """1
1
4
1 2 3 4
4
2 4 5 6
1
1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()