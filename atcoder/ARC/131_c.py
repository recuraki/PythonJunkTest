import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        board = 0
        full = set()
        for x in dat:
            full.add(x)
            board ^= x
        turn = 0 # 0 = I, 1 = E86
        while board != 0:
            x = -1
            if board in full:
                x = board
            else:
                for xx in full:
                    if (board^xx) in full:
                        x = xx
                        break
                    if x != -1: break
            if x == -1: break
            board ^= x
            full.remove(x)
            turn = 1 - turn

        if turn == 0: print("Lose")
        else: print("Win")

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
9 14 11 3 5 8"""
        output = """Lose"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
131"""
        output = """Win"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
12 23 34 45 56 78 89 98"""
        output = """Win"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()