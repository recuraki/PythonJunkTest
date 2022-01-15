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
        ans = INF
        oh, ow, sh, sw, gh, gw = map(int, input().split())
        if sh == gh or sw == gw:
            print(0)
            return
        if   sh < gh:
            ans = min(ans, gh - sh)
        elif sh > gh:
            ans = min(ans, 2*abs(oh - sh) + abs(sh - gh) )
        if   sw < gw:
            ans = min(ans, gw - sw)
        elif sw > gw:
            ans = min(ans, 2*abs(ow - sw) + abs(sw - gw) )
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
        input = """5
10 10 6 1 2 8
10 10 9 9 1 1
9 8 5 6 2 1
6 9 2 2 5 8
2 2 1 1 2 1"""
        output = """7
10
9
3
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()