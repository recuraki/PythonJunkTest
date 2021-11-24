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
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        s = input()
        num0 = s.count("0")
        num1 = s.count("1")
        t = ("0" * num0) + ("1" * num1)
        if s == t:
            print(0)
            return
        l = []
        for i in range(n):
            if s[i] != t[i]: l.append(i+1)
        ans = [len(l)] + l
        print(1)
        print(" ".join(list(map(str, ans))))

    # n questions
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
        input = """3
7
0011111
5
10100
6
001000"""
        output = """0
1
4 1 3 4 5
1
2 3 6"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()