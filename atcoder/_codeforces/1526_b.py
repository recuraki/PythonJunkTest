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
    # input = sys.stdin.readline

    from pprint import pprint
    def do():
        a = int(input())
        can = False
        for i in range(25):
            x = a - (111 * i)
            if x < 0:
                break
            if x % 11 == 0:
                #print(i, x // 11, i * 111 + (x // 11) * 11)
                can = True
        print("YES" if can else "NO")

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
        input = """3
33
144
69"""
        output = """YES
YES
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()