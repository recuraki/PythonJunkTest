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
        n = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        ans = INF
        f = lambda a, b: abs(a - b)

        # 1: box
        cost = 0
        cost += f(A[0], B[0])
        cost += f(A[-1], B[-1])
        ans = min(ans, cost)

        # 2: x
        cost = 0
        cost += f(A[0], B[-1])
        cost += f(A[-1], B[0])
        ans = min(ans, cost)

        # 3
        cost = 0
        cost += f(A[0], B[0])
        c1 = c2 = INF
        for i in range(n):
            c1 = min(c1, f(A[-1], B[i]))
        for i in range(n):
            c2 = min(c2, f(A[i], B[-1]))
        cost += c1 + c2
        ans = min(ans, cost)

        # 4
        cost = 0
        cost += f(A[0], B[-1])
        c1 = c2 = INF
        for i in range(n): c1 = min(c1, f(A[-1], B[i]))
        for i in range(n): c2 = min(c2, f(A[i], B[0]))
        cost += c1 + c2
        ans = min(ans, cost)

        # 5
        cost = 0
        cost += f(A[-1], B[-1])
        c1 = c2 = INF
        for i in range(n): c1 = min(c1, f(A[0], B[i]))
        for i in range(n): c2 = min(c2, f(A[i], B[0]))
        cost += c1 + c2
        ans = min(ans, cost)

        # 6
        cost = 0
        cost += f(A[-1], B[0])
        c1 = c2 = INF
        for i in range(n): c1 = min(c1, f(A[0], B[i]))
        for i in range(n): c2 = min(c2, f(A[i], B[-1]))
        cost += c1 + c2
        ans = min(ans, cost)

        # free
        cost = 0
        c1 = c2 = c3 = c4 = INF
        for i in range(n): c1 = min(c1, f(A[0], B[i]))
        for i in range(n): c2 = min(c2, f(A[-1], B[i]))
        for i in range(n): c3 = min(c3, f(A[i], B[0]))
        for i in range(n): c4 = min(c4, f(A[i], B[-1]))
        cost += c1 + c2 + c3 + c4
        ans = min(ans, cost)

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
        input = """2
3
1 10 1
20 4 25
4
1 1 1 1
1000000000 1000000000 1000000000 1000000000"""
        output = """31
1999999998"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()