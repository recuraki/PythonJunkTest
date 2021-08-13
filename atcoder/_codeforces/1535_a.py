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
        a,b,c,d = map(int, input().split())
        dat = [a,b,c,d]
        dat.sort(reverse=True)
        winwin = [dat[0], dat[1]]
        x1 = max(a,b)
        x2 = max(c,d)
        if x1 in winwin and x2 in winwin:
            print("YES")
        else:
            print("NO")

    q=int(input())
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
3 7 9 5
4 5 6 9
5 3 8 1
6 5 3 2"""
        output = """YES
NO
YES
NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()