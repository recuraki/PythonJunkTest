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
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        s = input()
        c = input()
        n = len(s)
        for i in range(n):
            if s[i] != c: continue
            l = i
            r = n - i - 1
            if l % 2 == 0 and r % 2 == 0:
                print("YES")
                return
        print("NO")



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
        input = """5
abcde
c
abcde
b
x
y
aaaaaaaaaaaaaaa
a
contest
t"""
        output = """YES
NO
NO
YES
YES"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()