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
    def do():
        _ = input()
        ax, ay = map(int, input().split())
        bx, by = map(int, input().split())
        fx, fy = map(int, input().split())
        diff = abs(ax-bx) + abs(ay-by)
        if ax == bx == fx:
            if min(ay,by) < fy < max(ay,by):
                print(diff + 2)
                return
        if ay == by == fy:
            if min(ax,bx) < fx < max(ax,bx):
                print(diff + 2)
                return
        print(diff)

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
        input = """7

1 1
3 3
2 2

2 5
2 1
2 3

1000 42
1000 1
1000 1000

1 10
3 10
2 10

3 8
7 8
3 7

2 1
4 1
1 1

1 344
1 10
1 1"""
        output = """4
6
41
4
4
2
334"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()