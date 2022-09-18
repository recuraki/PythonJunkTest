
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




    #import sys
    #input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        #print("---")
        #print(data, datb)
        maval = max(data)
        mbvam = max(datb)
        datc = []
        d = maval - mbvam
        if d < 0:
            print("NO")
            return
        for x in data:
            if (x - d) < 0: datc.append(0)
            else: datc.append(x-d)
        #print(data, datb, datc)
        if datb == datc:
            print("YES")
        else:
            print("NO")

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
4
3 5 4 1
1 3 2 0
3
1 2 1
0 1 0
4
5 3 7 2
1 1 1 1
5
1 2 3 4 5
1 2 3 4 6
1
8
0
1
4
6
"""
        output = """YES
YES
NO
NO
YES
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()