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
    #input = sys.stdin.readline


    from pprint import pprint
    def do():
        def f(cnt):

            if cnt == 0:
                return "DRAW"
            if cnt == 1:
                return "BOB"
            if cnt == 2:
                return "BOB"
            if cnt % 2 == 0:
                return "BOB"
            return "ALICE"


        def ff(s):
            return (f(s.count("0")))

        n = int(input())
        s = input()
        print(ff(s))

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
        input = """2
4
1001
1
0"""
        output = """BOB
BOB
DRAW
DRAW
BOB
ALICE"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """1
1
0000000
"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()