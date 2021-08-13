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

        def f(n):
            n = str(n)
            res = 0
            for i in range(len(n)):
                cnt = int("1" * (len(n) - i))
                res += (cnt * int(n[i]))
            return res

        l, r = map(int, input().split())
        print(f(r) - f(l))

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
1 9
9 10
10 20
1 1000000000"""
        output = """8
2
11
1111111110"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()