import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    dat = list(map(int, input().split()))
    #dat = [[i, datSource[i]] for i in range(n)]
    #dat.sort(key=lambda x: (-x[1], -x[0]))
    indL = 0
    indR = n - 1


    loop = math.ceil(n / 2)
    used = [False] * n # その数は使ったか？
    filled = [False] * n # 埋まっているか？
    res = 0
    while indR >= indL:
        # まずL
        maxindL = -1
        maxvalL = -9999999999999999999999
        maxindR = -1
        maxvalR = -9999999999999999999999

        for ind in range(n):
            if used[ind]: # もう使っているならパス
                continue
            disL = abs(ind - indL)
            if (dat[ind] * disL) > maxvalL:
                maxvalL = dat[ind] * disL
                maxindL = ind
            disR = abs(ind - indR)
            if (dat[ind] * disR) > maxvalR:
                maxvalR = dat[ind] * disR
                maxindR = ind

        #print(maxvalL, maxvalR)
        if maxvalL >= maxvalR: # L > R
            filled[indL] = True
            used[maxindL] = True
            res += maxvalL
            #print("L:", indL, "maxind", maxindL, "maxval", maxvalL)
            indL += 1
        else:
            filled[indR] = True
            used[maxindR] = True
            res += maxvalR
            #print("R:", indR, "maxind",maxindR, "maxval",maxvalR)
            indR -= 1
    print(res)





class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_0(self):
        print("test_input_0")
        input = """5
5 4 3 2 1"""
        output = """20"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """4
1 3 4 2"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
5 5 6 1 1 1"""
        output = """58"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
8 6 9 1 2 1"""
        output = """85"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()