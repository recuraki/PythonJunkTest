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
    from fractions import Fraction

    import math
    INF = 1 << 63

    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        ans = INF
        if n == 1:
            print(0)
            return
        for l in range(n):
            for r in range(l + 1, n):
                diff = Fraction(dat[r] - dat[l], (r - l))
                # print(l, r, diff)
                tmp = 0
                for i in range(n):
                    want = dat[l] - diff * (l - i)
                    # print(diff,"center",center, tmp, i, "want", want, "dat[i]", dat[i])
                    if want != dat[i]: tmp += 1
                # print(diff, center, tmp)
                ans = min(ans, tmp)

        print(ans)

    # n questions
    q = int(input())
    for qq in range(q):
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
4
1 2 3 4
4
1 1 2 2
2
0 -1
6
3 -2 4 -1 -4 0
1
-100"""
        output = """0
2
0
3
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()