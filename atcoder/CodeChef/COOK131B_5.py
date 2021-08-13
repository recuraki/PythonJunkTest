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

    INF = 1 << 63
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        mm = max(dat)
        param = 0
        for i in range(n-1):
            if dat[i] != dat[i+1]: param += 1
        print(param)
        # pyon
        newdat = []
        newdat.append(dat[0])
        for i in range(1, n-1):
            if param <= k: continue
            if dat[i-1] != dat[i] and dat[i] != dat[i+1]:
                param -= 2
            newdat.append(dat[i])
        newdat.append(dat[-1])
        

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
4 1
1 1 2 3
9 2
1 2 3 2 4 5 6 7 5
5 5
1 1 1 1 1
10 1
1 2 1 2 1 2 1 2 1 2"""
        output = """3
5
5
6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input
                      , output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()