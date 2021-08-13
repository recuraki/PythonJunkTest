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
        if total % n != 0:
            print(-1)
            return
        per = total // n
        res = 0
        for x in dat:
            if x > per:
                res += 1
        print(res)

    q = int(input())
    for _ in range(q):
        do()
    # do()




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
4
4 5 2 5
2
2 4
5
10 8 5 1 4
1
10000
7
1 1 1 1 1 1 1"""
        output = """2
1
-1
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()