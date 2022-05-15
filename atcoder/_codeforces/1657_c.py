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



    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    # c = 行える回数
    # r = 残った数
    class cumSum1D(object):
        sdat = []

        def init(self):
            pass

        def load(self, l):
            import itertools
            self.sdat = list(itertools.accumulate(itertools.chain([0], l)))

        def query(self, l, r):
            """
            query [l, r)
            """
            # assert l < r
            return self.sdat[r] - self.sdat[l]
    def do():
        n = int(input())
        s = input()
        n = len(s)
        s = list(s)
        l = []

        opcnt = 0
        i = 0
        while True:
            if i == n: break
            if i == n - 1: break

            if s[i] == "(":
                s[i] = "_"
                s[i + 1] = "_"
                i += 2
                opcnt += 1
                continue
            elif s[i] == ")":
                if s[i + 1] == ")":
                    s[i] = "_"
                    s[i + 1] = "_"
                    i += 2
                    opcnt += 1
                    continue
                # (
                j = i + 1
                while (j <= n - 1) and s[j] == "(":
                    j += 1
                if j == n:
                    break
                for k in range(i, j + 1):
                    s[k] = "_"
                i = j + 1
                opcnt += 1
            else:
                assert False
        ans = 0
        for x in s:
            if x != "_": ans += 1
        print(opcnt, ans)

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
2
()
3
())
4
((((
5
)((()
6
)((()("""
        output = """1 0
1 1
2 0
1 0
1 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()