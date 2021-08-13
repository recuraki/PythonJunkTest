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

    INF = 1 << 63
    def do():
        n, k = map(int, input().split())
        l = list(map(int, input().split()))
        res = -INF
        #print("------------")
        for i in range(n):
            for j in range(i+1, min(n, i+21)):
                x = (i + 1) * (j + 1) - k * (l[i] | l[j])
                print(i+1, j+1, x)
                res = max(res, x)
        print(res)

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
        input = """4
3 3
1 1 3
2 2
1 2
4 3
0 1 2 3
6 6
3 2 0 0 5 6"""
        output = """-1
-4
3
12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()