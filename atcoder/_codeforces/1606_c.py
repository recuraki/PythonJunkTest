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
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = []
        for x in dat:
            buf.append(10**x)
        canbed = []
        for i in range(n-1):
            canbed.append(10 ** (dat[i+1] - dat[i]) - 1)
        #print(canbed)
        def needmaisuu(x):
            res = 0
            for i in range(len(buf) - 1, -1, -1):
                need = x // buf[i]
                x -= need * buf[i]
                res += need
            return res
        tanni = sum(canbed)
        #print("tanni",tanni)
        k += 1
        ans = [0] * n
        for i in range(len(canbed)):
            x = min(canbed[i], k)
            k -= x
            ans[i] = x
        ans[-1] = k
        #print(ans, k)
        res = 0
        for i in range(n):
            res += buf[i] * ans[i]
        print(res)


    # n questions
    q = int(input())
    for _ in range(q):
        do()



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        self.maxDiff = 1000000
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
3 13
0 1 2
2 777
0 4
3 255
0 1 3
10 1000000000
0 1 2 3 4 5 6 7 8 9"""
        output = """59
778
148999
999999920999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()