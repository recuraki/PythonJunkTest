import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        mod = 998244353
        hh, ww = map(int, input().split())
        maze = []
        for h in range(hh):
            l = list(input())
            maze.append(l)

        cnt = 1

        for initw in range(ww):
            #print("initw", initw)
            w = initw
            initchar = maze[0][w] # fixed or R or B
            for h in range(1, hh):
                w -= 1
                #print(">", h, w)
                if w < 0:
                    #print("b1")
                    break
                if maze[h][w] == ".": # allなら気にしない
                    #print("b2")
                    continue
                if initchar == ".": # いまが、allなら、
                    #print("b3")
                    initchar = maze[h][w] # その色にする
                    continue
                if initchar != maze[h][w]: # バイオレーションが起こるとき
                    #print("b4")
                    print(0) #つくれない
                    return
            if initchar == ".":
                #print("okok")
                cnt *= 2
                cnt %= mod

        for inith in range(1, hh):
            h = inith
            w = ww
            initchar = maze[h][w-1]
            #print("inith", inith, initchar)
            for h in range(inith, hh):
                w -= 1
                #print(">", h, w)
                if w < 0:
                    break
                if maze[h][w] == ".": # allなら気にしない
                    continue
                if initchar == ".": # いまが、allなら、
                    initchar = maze[h][w] # その色にする
                    continue
                if initchar != maze[h][w]: # バイオレーションが起こるとき
                    print(0) #つくれない
                    return
            if initchar == ".":
                #print("okok")
                cnt *= 2
                cnt %= mod

        print(cnt)
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
        input = """2 2
B.
.R"""
        output = """2"""
        #self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3
R.R
BBR
..."""
        output = """0"""
        #self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 2
BB
BB"""
        output = """1"""
        #self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """3 3
.BB
BBB
BB."""
        output = """4"""
        self.assertIO(input, output)
    def test_input_311(self):
        print("test_input_311")
        input = """3 3
BBB
BBB
BBB"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3111(self):
        print("test_input_3111")
        input = """3 3
BB.
B.B
.BB"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()