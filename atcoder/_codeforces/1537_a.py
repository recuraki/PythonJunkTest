
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
        if (total / n )==1 and total % n == 0:
            print(0)
            return
        if (total / n) > 1:
            need = total
            print(need - n)
            return
        else:
            print(1)
            return



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
3
1 1 1
2
1 2
4
8 4 6 2
1
-2"""
        output = """0
1
16
1"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """1
2
-10 -10
"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()