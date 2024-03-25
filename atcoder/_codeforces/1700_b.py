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








    q = int(input())
    for _ in range(q):
        n,s = int(input()), int(input())
        if str(s)[0] != "9": print(int("9" * n) - s)
        else: print(int("1" * (n+1)) - s)




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
99
4
1023
3
385"""
        output = """32
8646
604"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """2
1
0
1
9"""
        output = """9
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()