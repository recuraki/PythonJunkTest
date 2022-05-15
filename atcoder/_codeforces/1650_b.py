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
        l, r, a = map(int, input().split())
        can = [l, r]
        can.append(l // a)
        can.append(a*(l // a) + 1)
        can.append(a*(r // a) - 1)
        can.append(a*(l // a) - 1)
        can.append(a*(r // a) + 1)
        can.append(a*(l // a + 1))
        can.append(a*(r // a - 1))
        can.append(a*(l // a - 1))
        can.append(a*(r // a + 1))
        can.append(a*(r // a))
        can.append(a*(r // a))

        can.append(l + 1)
        can.append(r - 1)
        can.append(l + 2)
        can.append(r - 2)

        ans = -INF
        for x in can:
            if l <= x <= r:
                x = x // a + x%a
                ans = max(ans, x)
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
1 4 3
5 8 4
6 10 6
1 1000000000 1000000000
10 12 8"""
        output = """2
4
5
999999999
5"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()