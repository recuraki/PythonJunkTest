import math
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
    import math

    INF = 1 << 63
    def do():
        n = int(input())
        res = INF
        from math import ceil


        for s8 in range(10):
            # s8-mai
            nokori = n - (8* s8)
            x = 20 * s8
            if nokori <= 0:
                res = min(res, x)
                continue
            ox = x
            onokori = nokori

            for s10 in range(10):
                x = ox
                nokori = onokori
                #print(s8, s10, x, nokori)
                nokori = nokori - (10 * s10)
                x += 25 * s10
                #print(s8, s10, x, nokori)
                if nokori <= 0:
                    res = min(res, x)
                    continue

                x += 15 * math.ceil(nokori / 6)
                res = min(res, x)

        print(res)

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
12
15
300
1
9999999999999999
3"""
        output = """30
40
750
15
25000000000000000
15"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
9
"""
        output = """25"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()