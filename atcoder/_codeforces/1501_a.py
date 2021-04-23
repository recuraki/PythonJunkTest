import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    def do():
        import math
        n = int(input())
        buf = []

        for i in range(n):
            a,b = map(int, input().split())
            buf.append( (a,b) )
        dat = list(map(int, input().split()))
        cur = buf[0][0] + dat[0]
        for i in range(n - 1):
            # cur = 到着時間
            a, b = buf[i]
            mindept = b
            minwait = cur + math.ceil((b - a) / 2)

            # 次に到着する時間
            cur = max(mindept, minwait) + buf[i+1][0] - b
            cur += dat[i+1]
        print(cur)


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
2
2 4
10 12
0 2
5
1 4
7 8
9 10
13 15
19 20
1 2 3 4 5"""
        output = """12
32"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_12")
        input = """1
1
10 0
1 
"""
        output = """2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()