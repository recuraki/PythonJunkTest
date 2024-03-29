import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

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
        n, x = map(int, input().split())
        ans = INF
        dat = []
        for i in range(n):
            a, b = map(int, input().split())
            dat.append( (a, b) )
        mingame = INF
        base = 0
        for i in range(n): # ステージiまでクリアしたとする
            story, game = dat[i]
            base += story + game # これが基本出かかる
            mingame = min(mingame, game)
            nokori = x - i - 1
            cur = base + mingame * nokori
            ans = min(ans, cur)
            if nokori <= 0: break
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
        input = """3 4
3 4
2 3
4 2"""
        output = """18"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 1000000000
3 3
1 6
4 7
1 8
5 7
9 9
2 4
6 4
5 1
3 1"""
        output = """1000000076"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()