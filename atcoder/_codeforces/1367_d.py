import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    import collections
    for _ in range(q):
        s = input()
        m = int(input())
        dat = list(map(int, input().split()))
        l = len(dat)
        datc = collections.Counter(s)
        buf = []
        for k in datc:
            buf.append([k, datc[k]])
        buf.sort(reverse=True)
        #print(buf)
        fixedNum = 0
        decidedPositions = []
        captalIndex = 0
        finalstr = [None] * l
        while True:
            candidatePos = []

            for i in range(l):
                if i in decidedPositions:
                    continue # is desided skip
                cnt = 0 # This Char (cursor=i)
                for j in range(len(decidedPositions)):
                    cnt += abs(decidedPositions[j] - i)
                if cnt == dat[i]:
                    candidatePos.append(i)

            candidateNum = len(candidatePos)
            while buf[captalIndex][1] < candidateNum:
                captalIndex += 1
            fixedChar = buf[captalIndex][0]
            captalIndex += 1

            #print("deside: {0} is {1}".format(candidatePos, fixedChar))

            for ind in candidatePos:
                finalstr[ind] = fixedChar
                decidedPositions.append(ind)
            fixedNum += candidateNum

            if fixedNum == l:
                break
            #print("next")

        #print("RES!")
        print("".join(finalstr))






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
abac
3
2 1 0
abc
1
0
abba
3
1 0 1
ecoosdcefr
10
38 13 24 14 11 5 3 24 17 0"""
        output = """aac
b
aba
codeforces"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()