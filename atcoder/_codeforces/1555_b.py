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
        def dd(s):
            return
        import math
        roomw, roomh = map(int, input().split())
        x1,y1,x2,y2 = map(int, input().split())
        #print("toomsize wh", roomw, roomh)
        #print(x1,y1,x2,y2)
        #print("tablesize wh", tablew, tableh)
        boxw, boxh = list(map(int, input().split()))
        canh = canw = False
        # phase1: tate
        # pat1 bottom
        res = INF


        tablew = x2 - x1
        tableh = y2 - y1
        for pat in [0,1,2,3]:
            moveh = movew = INF
            # h
            if pat in [0, 2]:
                if y1 >= boxh: moveh = 0
                else:
                    if boxh + tableh <= roomh:  moveh = boxh - y1
            if pat in [1,3]:
                tmp = roomh - boxh
                if y2 <= tmp: moveh = 0
                else: #must move
                    if boxh + tableh <= roomh: moveh = y2 - tmp
            # w
            if pat in [0, 1]:
                if x1 >= boxw: movew = 0
                else: #must move
                    if boxw + tablew <= roomw: movew = boxw - x1
            if pat in [2, 3]:
                tmp = roomw - boxw
                if x2 <= tmp: movew = 0
                else:
                    if boxw + tablew <= roomw: movew = x2 - tmp

            res = min(movew, moveh, res)
        if res == INF: res = -1
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
        input = """5
8 5
2 1 7 4
4 2
5 4
2 2 5 4
3 3
1 8
0 3 1 6
1 5
8 1
3 0 6 1
5 1
8 10
4 5 7 8
8 5"""
        output = """1.000000000
-1
2.000000000
2.000000000
0.000000000"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """1
8 1
3 0 6 1
5 1
"""
        output = """2"""
        #self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()