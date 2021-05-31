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
        n = int(input())
        dat = list(map(int, input().split()))
        can = True
        for i in range(n):
            if dat[i] == i+1:
                continue
            can = False
            break
        if can:
            print(0)
            return
        if dat[0] == n and dat[n-1] == 1:
            print(3)
            return
        if dat[0] == 1 or dat[n-1] == n:
            print(1)
            return
        print(2)
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
        input = """3
4
1 3 2 4
3
1 2 3
5
2 1 4 5 3"""
        output = """1
0
2"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """6
3
1 2 3
3
1 3 2
3
2 1 3
3
2 3 1
3
3 1 2
3
3 2 1
"""
        output = """0
1
1
2
2
3"""
        self.assertIO(input, output)

    def test_input_122(self):
        print("test_input_122")
        input = """1
5
5 4 3 2 1
"""
        output = """3"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()