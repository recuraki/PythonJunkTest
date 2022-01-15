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


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n, a, b = map(int, input().split())
        if abs(a-b) > 1:
            print(-1)
            return
        if (a+b) > (n-2):
            print(-1)
            return
        dat = list(range(1, n + 1))
        l, r = 0, n-1
        ans = []
        if a == b == 0:
            ans = list(range(1, n + 1))
        else:
            if a == b or a > b:
                ans.append(dat[0])
                ans.append(dat[-1])
                l += 1
                r -= 1
                leftTurn = True
            else: # a < b
                ans.append(dat[-1])
                ans.append(dat[0])
                l += 1
                r -= 1
                leftTurn = False
            while (a+b) > 1:
                #print(ans, a, b)
                if leftTurn:
                    ans.append(dat[l])
                    l += 1
                    a -= 1
                else:
                    ans.append(dat[r])
                    r -= 1
                    b -= 1
                leftTurn = not leftTurn
            #print("end", ans,a, b)
            if a == 1:
                while l <= r:
                    ans.append(dat[r])
                    r -= 1
                    a -= 1
            if b == 1:
                while l <= r:
                    ans.append(dat[l])
                    l += 1
                    b -= 1


        def f(p):
            a = 0
            b = 0
            for i in range(1, len(p) - 1):
                if p[i - 1] < p[i] and p[i] > p[i + 1]: a += 1
                if p[i - 1] > p[i] and p[i] < p[i + 1]: b += 1
            print(p, a, b)
        print(" ".join(list(map(str, ans))))
        #f(ans)





    # n questions
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
4 1 1
6 1 2
6 4 0"""
        output = """1 3 2 4
4 2 3 1 5 6
-1"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """3
9 0 1
9 1 0
9 0 0"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()