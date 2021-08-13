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
        n, a, b = map(int, input().split())
        if a == 1:
            if (n - 1) % b == 0: print("Yes")
            else: print("No")
            return
        x = 1
        while x <= n:
            tarinai = n - x
            if tarinai % b == 0:
                print("Yes")
                return
            x *= a
        print("No")


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
        input = """5
24 3 5
10 3 6
2345 1 4
19260817 394 485
19260817 233 264"""
        output = """Yes
No
Yes
No
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()