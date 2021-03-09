import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    import collections
    import math
    input = sys.stdin.readline
    mnum = 10 ** 6 + 1000
    mnumsqr = math.ceil(math.sqrt(mnum)) + 10
    # mCanDivSqrt[x]  x can div max(sqrt num)
    # ex. 80 can be dived 4(2^2) or 16(4^2)
    #     this table ret maxnum = 16
    mCanDivSqrt = [-1] * (mnum + 10)
    for i in range(2, mnumsqr):
        if i ** 2 < mnum + 1:
            cur = i**2
            x = cur
            while x <= mnum:
                mCanDivSqrt[x] = i**2
                x += cur
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        numbTable = collections.defaultdict(int)
        for x in dat:
            while True: # make b-number
                if mCanDivSqrt[x] != -1:
                    x //= mCanDivSqrt[x]
                else: break
            numbTable[x] += 1
        nextBnum1 = numbTable[1] # anytime, 1 is good
        res0 = max(nextBnum1,1) # res0 is time=0 max adj
        for k in numbTable.keys(): # check all b num!
            if k == 1: continue
            res0 = max(res0, numbTable[k])
            if numbTable[k] % 2 == 0: # even count is good
                nextBnum1 += numbTable[k] # this bnum will be bnum=1
        nextBnum1=max(nextBnum1, res0)

        q = int(input())
        for _ in range(q):
            qnum = int(input())
            if qnum == 0: print(res0)
            else: print(nextBnum1)

    q = int(input())
    for _ in range(q): do()



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_0(self):
        print("test_input_0")
        input = """1
4
2 2 2 4
2
0
1
"""
        output = """3
3"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3
4
6 8 4 2
1
0
6
12 3 20 5 80 1
1
1
5
4 12 3 9 25
3
0
1
2"""
        output = """2
3
3
5
5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
40
1 3 5 6 2 10 7 10 4 2 10 10 6 1 1 8 1 3 7 2 9 10 4 2 4 1 9 1 1 4 1 7 8 1 7 9 3 10 7 1
40
1
7
0
5
1
9
9
2
0
5
7
7
3
10
4
6
0
9
0
8
5
5
3
3
6
5
1
10
8
8
3
1
1
4
7
1
5
8
4
1
"""
        output = """31
31
17
31
31
31
31
31
17
31
31
31
31
31
31
31
17
31
17
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31
31"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()