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
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        #print()
        data.sort()
        datb.sort()
        #print(data)
        #print(datb)
        can = True
        for i in range(n):
            if data[i] == datb[i] or data[i]+1 == datb[i]: continue
            else:
                print("NO")
                return
        print("YES")
        return

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
        input = """3
3
-1 1 0
0 0 2
1
0
2
5
1 2 3 4 5
1 2 3 4 5"""
        output = """YES
NO
YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()