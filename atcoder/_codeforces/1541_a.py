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
        dat = []
        for i in range(n):
            dat.append(i)
        for i in range(n-1):
            if dat[i] == i:
                dat[i], dat[i+1] = dat[i+1], dat[i]
        if dat[n-1] == n-1:
            dat[n-2], dat[n-1] = dat[n-1], dat[n-2]

        for i in range(n):
            dat[i] += 1
        print(" ".join(list(map(str, dat))))




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
2
3"""
        output = """2 1 
3 1 2 """
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """2
4
100"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()