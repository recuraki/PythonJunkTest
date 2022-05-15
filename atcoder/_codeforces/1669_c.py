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
        dat = list(map(int, input().split()))
        def check():
            a = dat[0] % 2
            for x in dat:
                if (x%2) != a:
                    return False
            return True

        if check():
            print("YES")
            return

        for i in range(0, n, 2):
            dat[i] += 1
        if check():
            print("YES")
            return

        for i in range(1, n, 2):
            dat[i] += 1
        if check():
            print("YES")
            return

        for i in range(1, n, 2):
            dat[i] += 1
        if check():
            print("YES")
            return

        print("NO")



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
3
1 2 1
4
2 2 2 3
4
2 2 2 2
5
1000 1 1000 1 1000"""
        output = """YES
NO
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()