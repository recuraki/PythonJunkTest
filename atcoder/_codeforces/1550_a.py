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
        total = 0
        num = 0
        i = 1
        while True:
            total += i
            num += 1
            if total >= n:
                break
            i += 2
        print(num)


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
1
8
7
42"""
        output = """1
3
3
7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
2"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()