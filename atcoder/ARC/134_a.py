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
        c = lambda a, b : (((a) + ((b) - 1)) // (b))
        n, l, w = map(int, input().split())
        dat = list(map(int, input().split()))
        covered = 0 # ここまでカバーされている
        ans = 0
        for i in range(n):
            target = dat[i]
            if covered < target: # t までの補強が必要
                need = c((target - covered) , w)
                covered += need * w
                ans += need
            covered = max(covered, target + w)
        if covered < l: # 右までいる
            need = c((l - covered) , w)
            covered += need * w
            ans += need
        print(ans)

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
        input = """2 10 3
3 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 10 3
0 1 4 6 7"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """12 1000000000 5
18501490 45193578 51176297 126259763 132941437 180230259 401450156 585843095 614520250 622477699 657221699 896711402"""
        output = """199999992"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1 2 1
0"""
        output = """1"""
if __name__ == "__main__":
    unittest.main()