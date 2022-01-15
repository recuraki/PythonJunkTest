import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    def do():
        #print()
        n = int(input())
        dat = []
        for _ in range(n):
            dat.append(["."] * n)
        c = 0
        for h in range(n):
            for i in range(3):
                dat[h][c] = "#"
                c = (c+1) % n

        if n % 3 == 0: # 倍数の時の処理
            for l in dat:
                print("".join(l))
            return
        # 倍数以外
        s1 = "".join(dat[0])
        s2 = "".join(dat[-1])
        #for l in dat:
        #    print("".join(l))
        #print("---")
        flag1 = 0
        flag2 = 0
        for i in range(1, n-1):
            l = dat[i]
            if l[0] == "#":
                flag1 += 1
                if flag1 == 1:
                    print(s1)
            print("".join(l))
            if l[0] == "#":
                flag2 += 1
                if flag2 == 2:
                    print(s2)
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
        input = """6"""
        output = """##..#.
##..#.
..##.#
..##.#
##...#
..###."""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """7"""
        output = """"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_1")
        input = """8"""
        output = """"""
        self.assertIO(input, output)
    def test_input_211(self):
        print("test_input_1")
        input = """9"""
        output = """"""
        self.assertIO(input, output)
    def test_input_2111(self):
        print("test_input_1")
        input = """31"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()