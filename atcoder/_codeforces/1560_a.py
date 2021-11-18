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
        k = int(input())
        x = 0
        while k > 0:
            x += 1
            if x % 10 == 3:
                continue
            if x % 3 == 0:
                continue
            k -= 1
        print(x)
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
        input = """10
1
2
3
4
5
6
7
8
9
1000"""
        output = """1
2
4
5
7
8
10
11
14
1666"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()