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
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        from collections import defaultdict
        d = defaultdict(int)
        for x in dat: d[x] += 1
        ans = 0
        for x in dat:
            if d[x] == 0: continue # もう使われている
            d[x] -= 1 # 何が何でも使う
            if x % k != 0: #割り切れない場合は足すしかないので
                ans += 1
                continue
            target = x // k
            if d[target] > 0:
                d[target] -= 1
            else: #数がない
                ans += 1
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
4 4
1 16 4 4
6 2
1 2 2 2 4 7
5 3
5 2 3 5 15
9 10
10 10 10 20 1 100 200 2000 3"""
        output = """0
2
3
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()