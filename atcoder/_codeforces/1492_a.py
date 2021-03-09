
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        p, a, b, c = map(int, input().split())
        res = 10** 250
        for val in [a,b,c]:
            x = p % val
            if x == 0:
                print(0)
                return
            res = min(res, val - x)
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
9 5 4 8
2 6 10 9
10 2 5 10
10 9 9 9"""
        output = """1
4
0
8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()