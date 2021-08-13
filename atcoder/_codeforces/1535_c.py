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
    def sigma1(n):
        return n * (n + 1) // 2

    import sys
    from pprint import pprint
    def do():
        s = input()




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
0?10
???
?10??1100
"""
        output = """8
6
25"""
        #self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
0???1
"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()