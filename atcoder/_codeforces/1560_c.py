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


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    import math

    INF = 1 << 63
    def do():
        n = int(input())
        # 1 = 1
        # 2,3,4 = 2
        # 5,6,7,8,9 = 3
        a = math.ceil(math.sqrt(n))
        amari = n - (a-1) ** 2
        amari -= 1
        #print(n, "amama", a, amari)
        if amari < a:
            print(amari + 1, a)
        else:
            print(a, a - (amari - (a-1) ))

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
11
14
5
4
1
2
1000000000"""
        output = """2 4
4 3
1 3
2 1
1 1
1 2
31623 14130"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1
2
3
4
5
6
7
8
9
10"""
        output = """1 1
1 2
2 2
2 1
1 3
2 3
3 3
3 2
3 1
1 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()