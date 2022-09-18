
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
        x = int(input())
        y = 0
        for i in range(1000):
            if (x>>i) & 1 == 1:
                y = 1 << i
                break
        #print(x, y)
        i = 0
        while True:
            if x ^ y > 0: break
            z = y | 1 << i
            if x ^ z > 0:
                y = z
            i += 1


        print(y)



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
        input = """7
1
2
5
9
16
114514
1000000"""
        output = """3
3
1
1
17
2
64"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()