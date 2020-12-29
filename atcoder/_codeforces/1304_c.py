import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        f = True
        curTime = 0
        canLow = canHigh = m
        dat = []
        for _ in range(n):
            visitTime, needLow, needHigh = map(int, input().split())
            dat.append((visitTime, needLow, needHigh))
        for visitTime, needLow, needHigh in dat:
            deltaTime = visitTime - curTime
            canLow -= deltaTime
            canHigh += deltaTime
            if needHigh < canLow or canHigh < needLow:
                f = False
            curTime = visitTime
            canLow = max(needLow, canLow)
            canHigh = min(needHigh, canHigh)
        print("YES" if f else "NO")

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
1 100
99 -100 0
3 0
5 1 2
7 3 5
10 -1 0
2 12
5 7 10
10 16 20
3 -100
100 0 0
100 -50 50
200 100 100"""
        output = """NO
YES
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()