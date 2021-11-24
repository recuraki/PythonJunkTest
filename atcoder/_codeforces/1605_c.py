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

    import math
    INF = 1 << 63
    def do():
        n = int(input())
        s = input()
        dat = []
        for x in s:
            if x == "a": dat.append(0)
            elif x == "b": dat.append(1)
            elif x == "c": dat.append(2)
        num0 = num1 = num2 = 0
        l = 0
        ans = -1
        for r in range(2):
            if dat[r] == 0: num0 += 1
            elif dat[r] == 1: num1 += 1
            elif dat[r] == 2: num2 += 1
        print(num0, num1, num2)
        if num0 == 2: ans = 2
        for r in range(2, n):









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
2
aa
5
cbabb
8
cacabccc"""
        output = """2
-1
3
"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()