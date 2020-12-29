import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        # first wall
        canLow, canHigh = dat[0]+1, dat[0] + k-1+1
        for i in range(1, n-1):
            maxCurBlock = dat[i] + (k-1) + k
            if maxCurBlock < canLow: # current block can reach prev block?
                print("NO")
                return
            if canHigh <= dat[i]: # prev block cannot reach current ground?
                print("NO")
                return
            canLow = max(dat[i] + 1, canLow - (k-1))
            canHigh = min(maxCurBlock, canHigh + (k-1))
        # last wall
        if (canLow - dat[n-1]) > k:
            print("NO") # n-1 wall is too high
            return
        if canHigh <= dat[n-1]:
            print("NO") # last wall's ground is too high
            return
        print("YES")

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
        input = """3
6 3
0 0 2 5 1 1
2 3
0 2
3 2
3 0 2"""
        output = """YES
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()