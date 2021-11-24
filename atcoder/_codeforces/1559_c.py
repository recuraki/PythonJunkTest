import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
- グラフをsetでたどろうとしていませんか？
REの時のポイント
- inputしきっていますか？

"""

def resolve():

    """
    n = 3:
    1,2,3,4 の場合、1->2->3
    までの道は作られる。
    0がないと絶対に成立しない
    """


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = []
        if dat[-1] == 0: # last go
            for i in range(n): res.append(i)
            res.append(n)
            print(" ".join(list(map(lambda x: str(x + 1), res))))
            return
        if dat[0] == 1: # last go
            res.append(n)
            for i in range(n): res.append(i)
            print(" ".join(list(map(lambda x: str(x + 1), res))))
            return
        for i in range(n - 1):
            if dat[i] == 0 and dat[i+1] == 1:
                for j in range(i+1): res.append(j)
                res.append(n)
                for j in range(i+1, n): res.append(j)
                print(" ".join(list(map(lambda x: str(x + 1), res))))
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
        input = """7
3
0 1 0
3
1 1 0
3
0 0 0
3
1 1 1
1
0
1
1
5
0 0 0 1 1
"""
        output = """1 2 3 4
1 2 3 4
1 2 3 4
4 1 2 3
1 2
2 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()