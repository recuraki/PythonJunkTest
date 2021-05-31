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
        s = input()
        n = int(input())
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))

    q = int(input())
    for _ in range(q):
        do()
    # do()


    dat = [1, 2, 3]
    print(" ".join(list(map(str, res))))

    pass
    #sys.setrecursionlimit(100000)
    import math
    math.ceil(1.2)
    math.floor(1.2)
    round(1.2, 3)



    import sys
    read = sys.stdin.read
    n, *indata = map(int, read().split())
    dat = []
    offset = 0




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
7 12
1 2 3 4 9 10 11
R R L L R R R
2 10
1 6
R R
2 10
1 3
L L
1 10
5
R
7 8
6 1 7 2 3 5 4
R L R L L L L"""
        output = """1 1 1 1 2 -1 2
-1 -1
2 2
-1
-1 2 7 3 2 7 3"""
        self.assertIO(input, output)
        

if __name__ == "__main__":
    unittest.main()