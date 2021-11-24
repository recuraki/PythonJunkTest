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



"""
1. の最初に小さいのを持ってくる
"""
def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        res = INF
        curmin = INF
        bufa = [-1] * (n)
        bufb = [-1] * (n)
        for i in range(n):
            bufa[data[i] // 2] = i
            bufb[(datb[i]-2) // 2] = i

        for i in range(n-1, -1, -1):
            curmin = min(curmin, bufb[i])
            t = bufa[i] + curmin
            res = min(res, t)

        print(res)

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
2
3 1
4 2
3
5 3 1
2 4 6
5
7 5 9 1 3
2 4 6 10 8"""
        output = """0
2
3"""
        self.assertIO(input, output)




if __name__ == "__main__":
    unittest.main()