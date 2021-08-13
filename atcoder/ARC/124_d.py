import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        def isL(x):
            if x < n: return True
            return False
        def isR(x):
            if n <= x: return True
            return False



        n, m = map(int, input().split())
        dat = list(map(lambda x: int(x) - 1, input().split()))
        import math
        res = 0
        print(dat)
        buffer = set()
        workbufferIndexL = 0
        workbufferIndexR = n
        basketL = set()
        basketR = set()

        pos = [None] * (n + m)
        for i in range(n + m):
            pos[dat[i]] = i
        for i in range(n):
            # ずれている子がいるならそれをworkにする
            if i != dat[i] and workbufferIndexL is None:
                workbufferIndexL = i
            basketL.add(dat[i])
        for i in range(m):
            # ずれている子がいるならそれをworkにする
            if n+i != dat[n+i] and workbufferIndexR is None:
                workbufferIndexR = n+i
            basketR.add(dat[n+i])
        print(buffer)

        res = 0
        def trans(a, b): # 座標a と 座標bをswap
            dat[a], dat[b], pos[dat[a]], pos[dat[b]] =  dat[b],dat[a],  pos[dat[b]],pos[dat[a]]


        # STEP1
        for i in range(n):
            x = dat[i] #この数
            if x == i: continue # 目標にもういるなら何もしない
            if i in basketR: # この数が向こうにいるものならもらう
                res += 1
                dat[pos[i]] = x
                dat[i] = i
                pos[x] = pos[i]
                pos[i] = i
                continue
            # そうでないならこっちにいる数
            if isR(x): # この数が向こうに送るべき数なら
                res += 1
                pos[i], pos[x]








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

    def test_input_11(self):
        print("test_input_11")
        input = """2 3
1 4 2 3 5"""
        output = """3"""
        self.assertIO(input, output)


    def test_input_1(self):
        print("test_input_1")
        input = """2 3
1 4 2 5 3"""
        output = """3"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 7
9 7 12 6 1 11 2 10 3 8 4 5"""
        output = """10"""
        #self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()