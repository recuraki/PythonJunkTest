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
        from collections import defaultdict
        n = int(input())
        dat = list(map(int, input().split()))
        buf1 = []
        buf2 = []
        buf3 = []

        for i in range(n):
            x1 = abs(dat[i] - i*2)
            x2 = dat[i] + i*2
            buf1.append(x1)
            buf2.append(x2)
            buf3.append(abs(x1-x2))

        print(buf1)
        print(buf2)
        print(buf3)



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
4
2 4 1 3
5
6 9 1 9 6
2
13 37"""
        output = """10
12
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()