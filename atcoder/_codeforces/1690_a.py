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
    # import pypyjit
    # pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        n = int(input())
        on = n
        n -= 3
        ans = [n // 3] * 3
        ans[0] += 1
        ans[1] += 2
        ans[2] += 0
        n %= 3
        while n >= 3:
            n -= 3
            ans[0] += 1
            ans[1] += 1
            ans[2] += 1
        if n == 0:
            pass
        elif n == 1:
            ans[1] += 1
            n -= 1
        elif n == 2:
            ans[0] += 1
            ans[1] += 1
            n -= 2
        print(*ans)
        # print(ans , on)
        # if sum(ans)!= on or not(ans[2] < ans[0] < ans[1]):
        #    print("!!!!!!!!!!")

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
        input = """6
11
6
10
100000
7
8"""
        output = """4 5 2
2 3 1
4 5 1
33334 33335 33331
2 4 1
3 4 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()