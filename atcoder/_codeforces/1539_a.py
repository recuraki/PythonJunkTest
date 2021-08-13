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
        def sigma1(n):
            return n * (n + 1) // 2

        n, x, t = map(int, input().split())
        covermans = t // x
        flatman = max(0, n - covermans)
        #print(covermans, "flat", flatman)
        if covermans > n:
            print(sigma1(n-1))
            return
        #print(flatman * covermans, sigma1(covermans-1))
        res = flatman * covermans
        res += sigma1(covermans-1)
        print(res)


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
4 2 5
3 1 2
3 3 10
2000000000 1 2000000000"""
        output = """5
3
3
1999999999000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5 10 10"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()