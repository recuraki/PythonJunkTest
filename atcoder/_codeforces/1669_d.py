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




    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        s = input()
        t = []
        buf = []
        for x in s:
            if x == "W":
                if len(t) != 0:
                    buf.append(t)
                t = []
                continue
            t.append(x)
        if len(t) != 0:
            buf.append(t)
        for cur in buf:
            if len(cur) == 1:
                print("NO")
                return
            a = cur[0]
            diff = False
            for x in cur:
                if a != x:
                    diff = True
                    break
            if diff is False:
                print("NO")
                return
        print("YES")

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
        input = """12
5
BRBBW
1
B
2
WB
2
RW
3
BRB
3
RBB
7
WWWWWWW
9
RBWBWRRBW
10
BRBRBRBRRB
12
BBBRWWRRRWBR
10
BRBRBRBRBW
5
RBWBW"""
        output = """YES
NO
NO
NO
YES
YES
YES
NO
YES
NO
YES
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()