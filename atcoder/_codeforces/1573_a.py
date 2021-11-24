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


    INF = 1 << 63
    def do():
        n = int(input())
        s = input()
        res = 0
        for i in range(len(s) -1):
            x = int(s[i])
            if x == 0: continue
            res += 1
            res += int(x)
        res += int(s[-1])
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
        input = """7
3
007
4
1000
5
00000
3
103
4
2020
9
123456789
30
001678294039710047203946100020"""
        output = """7
2
0
5
6
53
115"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()