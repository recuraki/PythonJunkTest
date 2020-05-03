import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    oddlist = []
    evenlist = []
    so = 0
    se = 0
    oddSumList = []
    evenSumList = []
    oddSumList.append(0)
    evenSumList.append(0)
    for i in range(n):
        if i % 2 == 0:
            se += dat[i]
            evenSumList.append(se)
            evenlist.append(dat[i])
        else:
            so += dat[i]
            oddSumList.append(so)
            oddlist.append(dat[i])
    if n % 2 == 0:
        print(max(sum(evenlist), sum(oddlist)))
    else:
        needCount = n // 2 # 切り捨て
        res = -1000000000000000000000
        #print(oddSumList)
        #print(evenSumList)
        for i in range(needCount + 1):
            s1 = oddSumList[i]
            for j in range(needCount - i + 1):
                l2 = i + 1
                r2 = l2 + j
                s2 = evenSumList[r2] - evenSumList[l2]

                k  = needCount - i - j

                l3 = i + j
                r3 = l3 + k - 1
                s3 = oddSumList[r3] - oddSumList[l3]
                #print(i, j, k, i+j+k, s1, s2, s3,s1+s2+s3)
                res = max(res, s1+s2+s3)
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
        input = """6
1 2 3 4 5 6"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
-1000 -100 -10 0 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """27
18 -28 18 28 -45 90 -45 23 -53 60 28 -74 -71 35 -26 -62 49 -77 57 24 -70 -93 69 -99 59 57 -49"""
        output = """295"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()