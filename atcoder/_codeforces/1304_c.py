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
        canLow = m
        canHigh = m
        curTime = 0
        dat = []
        for _ in range(n):
            visitTime, needLow, needHigh = map(int, input().split())
            dat.append((visitTime, needLow, needHigh))

        for i in range(n):
            visitTime, needLow, needHigh = dat[i]
            deltaTime = visitTime - curTime
            canLow -= deltaTime
            canHigh += deltaTime
            if needHigh < canLow or canHigh < needLow:
                f = False
                break
            curTime = visitTime
            if needLow > canLow:
                canLow = needLow
            if needHigh < canHigh:
                canHigh = needHigh
        if f:
            print("YES")
        else:
            print("NO")

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

    def test_input_2(self):
        print("test_input_2")
        input = """10
2 9
12 -1 10
15 -1 10
2 7
5 -10 -8
17 -1 5
2 10
8 -8 7
16 -10 -5
2 -8
6 -6 7
18 -10 6
2 5
13 -10 -8
16 0 0
2 -7
15 -5 4
20 1 8
2 5
1 -10 2
8 -3 4
2 9
11 -8 9
14 -7 -2
2 8
1 -8 0
14 -6 1
2 7
5 2 9
13 -9 8
2 -1
12 -9 -7
19 -10 5
2 -5
10 -10 3
15 6 7
2 -10
3 6 9
12 1 4
2 -5
5 -8 -4
20 -6 4
2 10
3 -2 5
20 0 3
2 -9
2 -9 -3
18 -2 9
2 5
7 -8 6
15 -5 8
2 0
19 -4 2
20 -2 -1
2 2
9 -9 5
20 -10 4
2 -10
15 -7 -1
15 -6 -5
2 -5
10 -10 -1
15 -1 0
2 9"""
        output = """xxx"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()