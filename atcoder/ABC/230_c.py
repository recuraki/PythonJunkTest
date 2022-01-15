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
        n, a, b = map(int, input().split())
        p, q, r, s = map(int, input().split())
        ans = []
        # Q−P+1 行 出力。各行はS−R+1文字
        for i in range(p, q+1):
            l = ""
            for j in range(r, s+1):
                black = False
                # 状態1?
                k1 = i - a
                k2 = j - b
                if k1 == k2:
                    # hit?
                    if max(1-a, 1-b) <= k1 <= min(n-a, n-b):
                        black = True
                # 状態2?
                k1 = i - a
                k2 = b-j
                if k1 == k2:
                    # hit?
                    if max(1-a, b-n) <= k1 <= min(n-a, b-1):
                        black = True
                if black: print("#", end="")
                else: print(".", end="")
            print("")
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
        input = """5 3 2
1 5 1 5"""
        output = """...#.
#.#..
.#...
#.#..
...#."""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 3 3
4 5 2 5"""
        output = """#.#.
...#"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000"""
        output = """#.#
.#.
#.#"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()