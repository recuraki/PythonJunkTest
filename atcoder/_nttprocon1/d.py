import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    y, x = map(int,input().split())
    dat = []
    for i in range(y):
        a = list(map(int, input().split()))
        dat.append(a)
    s = input()

    #print("init")
    #print(dat)

    for i in range(len(s)):
        if s[i] == "U":
            #print("U")
            #pprint(dat)
            # まずマージ
            for xx in range(x):
                for yy in range(y):
                    for yyy in range(yy + 1, y):
                        #print("{0} {1} {2} {3}".format(yy,xx,yyy,xx))
                        if dat[yy][xx] == dat[yyy][xx]:
                            dat[yy][xx] *= 2
                            dat[yyy][xx] = 0
                            break
                        if dat[yyy][xx] != 0:
                            break
            #print("U MOVE")
            #pprint(dat)
            # 移動
            for xx in range(x):
                for yy in range(y):
                    if dat[yy][xx] == 0:
                        for yyy in range(yy + 1, y):
                            if dat[yyy][xx] != 0:
                                dat[yy][xx] = dat[yyy][xx]
                                dat[yyy][xx] = 0
                                break

            #print("U ed")
            #pprint(dat)
            pass

        elif s[i] == "D":
            #print("D")
            #pprint(dat)

            # まずマージ
            for xx in range(x):
                for yy in range(y - 1, -1, -1):
                    for yyy in range(yy - 1, -1, -1):
                        #print("{0} {1} {2} {3}".format(yy,xx,yyy,xx))
                        if dat[yy][xx] == dat[yyy][xx]:
                            dat[yy][xx] *= 2
                            dat[yyy][xx] = 0
                            break
                        if dat[yyy][xx] != 0:
                            break
            # 移動
            #print("D MOVE")
            #pprint(dat)
            for xx in range(x):
                for yy in range(y - 1, -1, -1):
                    if dat[yy][xx] == 0:
                        for yyy in range(yy - 1, -1, -1):
                            if dat[yyy][xx] != 0:
                                dat[yy][xx] = dat[yyy][xx]
                                dat[yyy][xx] = 0
                                break

            #print("D ed")
            #pprint(dat)
            pass

        elif s[i] == "R":
            #print("R")
            #pprint(dat)
            # まずマージ
            for xx in range(x - 1 , -1 , -1):
                for yy in range(y):
                    for xxx in range(xx - 1, -1, -1):
                        if dat[yy][xx] == dat[yy][xxx]:
                            dat[yy][xx] *= 2
                            dat[yy][xxx] = 0
                            break
                        if dat[yy][xxx] != 0:
                            break
            # 移動
            #print("R MOVE")
            #pprint(dat)
            for xx in range(x - 1, -1, -1):
                for yy in range(y):
                    if dat[yy][xx] == 0:
                        for xxx in range(xx - 1, -1, -1):
                            if dat[yy][xxx] != 0:
                                dat[yy][xx] = dat[yy][xxx]
                                dat[yy][xxx] = 0
                                break
            #print("Red")
            #pprint(dat)

        elif s[i] == "L":
            #print("L")
            #pprint(dat)
            # まずマージ
            for xx in range(x):
                for yy in range(y):
                    for xxx in range(xx + 1, x):
                        if dat[yy][xx] == dat[yy][xxx]:
                            dat[yy][xx] *= 2
                            dat[yy][xxx] = 0
                            break
                        if dat[yy][xxx] != 0:
                            break
            # 移動
            #print("L move")
            #pprint(dat)
            for xx in range(x):
                for yy in range(y):
                    if dat[yy][xx] == 0:
                        for xxx in range(xx + 1, x):
                            if dat[yy][xxx] != 0:
                                dat[yy][xx] = dat[yy][xxx]
                                dat[yy][xxx] = 0
                                break
            #print("L ed")
            #pprint(dat)

    #print(dat)
    for i in range(y):
        s = map(lambda x: str(x), dat[i])
        print(" ".join(s))



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
        input = """2 3
2 2 2
2 2 2
URDL"""
        output = """0 0 0
4 8 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 7
4 64 8 32 16 2 4
2 16 2 2 4 2 2
32 2 8 8 32 16 32
32 32 32 64 8 2 8
2 8 32 16 16 64 8
ULLURUD"""
        output = """0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 64 16 8
0 4 64 32 32 4 32
0 64 4 128 2 128 32"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()