
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # k = 1からnまでの k の和
    def sigma1(n):
        return n * (n + 1) // 2

    def do():
        l, r = map(int, input().split())
        #print("-",r,l)
        x = r - l
        x -= (l - 1)
        if x < 0:
            print(0)
            return
        #print(">>" , x)
        print(sigma1(x))

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
2 6
0 0
1000000 1000000
12345 67890
0 1000000"""
        output = """6
1
0
933184801
500001500001"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()