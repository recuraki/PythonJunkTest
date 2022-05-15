
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
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        tarinai = [0] * 31
        for x in dat:
            for j in range(31):
                if ((x >> j) & 1) == 0: tarinai[j] += 1
        #print(tarinai)
        ans = 0
        for j in range(30, -1, -1):
            if tarinai[j] <= k:
                k -= tarinai[j]
                ans = ans | (1<<j)
        print(ans)


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
        input = """4
3 2
2 1 1
7 0
4 6 6 28 6 6 12
1 30
0
4 4
3 1 3 1"""
        output = """2
4
2147483646
1073741825"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()