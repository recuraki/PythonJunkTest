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
        ans = 0
        oddcount = 0
        buf = []
        for x in dat:
            if x % 2 == 1:
                oddcount += 1
            else: # even
                cnt = 0
                o = x
                while o %2 == 0:
                    o //= 2
                    cnt += 1
                buf.append( (cnt, x) )
        buf.sort()
        #print(buf)
        if oddcount > 0:
            print(len(buf))
            return
        if len(buf) == 0:
            print(0)
            return
        ans = buf[0][0]
        ans += len(buf)-1
        print(ans)
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
        input = """4
2
1 9
3
1 1 2
3
2 4 8
3
1049600 33792 1280"""
        output = """0
1
3
10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5
3 100 200 300 400"""
        output = """4"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()