import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        a, b, c= map(int, input().split())
        a, b = min(a,b), max(a,b)
        n2 = b - a
        allmember = n2 * 2
        if not (1 <= a <= n2 and n2 < b <= allmember):
            print(-1)
            return
        if 1 <= c <= n2:
            print(c + n2)
        elif n2 < c <= allmember:
            print(c - n2)
        else:
            print(-1)
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
6 2 4
2 3 1
2 4 10
5 3 4
1 3 2
2 5 4
4 3 2"""
        output = """8
-1
-1
-1
4
1
-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()