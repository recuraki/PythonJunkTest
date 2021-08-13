import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        import math
        n = int(input())
        dat = list(map(int, input().split()))
        canmake = min(dat)
        can = True
        res = 0
        # try create base
        for x in dat:
            if x == canmake: continue
            canmax = math.ceil(x/2) - 1
            if canmake > canmax:
                can=False
                break
            res += 1
        if can:
            print(res)
            return
        print(n)

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
2 1 3
3
1 1 3
4
3 3 3 1"""
        output = """3
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()