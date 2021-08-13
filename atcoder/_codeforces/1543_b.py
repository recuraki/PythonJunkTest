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
        n = int(input())
        dat = list(map(int, input().split()))
        total = sum(dat)
        a = total % n
        b = n - a
        print(a*b)
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
3
1 2 3
4
0 1 1 0
10
8 3 6 11 5 2 1 7 10 4"""
        output = """0
4
21"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()