import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    def do():
        n = int(input()) // 2
        dat = []
        for i in range(2*n):
            dat.append(list(map(int, input().split())))
        for i in range(5):
            for j in range(i+1, 5):
                cani = canj = canboth = canno = 0
                for ind in range(2*n):
                    if dat[ind][i] == dat[ind][j] == 1: canboth += 1
                    elif dat[ind][i] == 1: cani += 1
                    elif dat[ind][j] == 1: canj += 1
                    else: canno += 1
                if canno > 0: continue
                if cani > n or canj > n: continue
                print("YES")
                return
        print("NO")
        return
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
1 0 0 1 0
0 1 0 0 1
0 0 0 1 0
0 1 0 1 0
2
0 0 0 1 0
0 0 0 1 0"""
        output = """YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()