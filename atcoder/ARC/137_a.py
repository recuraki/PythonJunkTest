import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        limitl, limitr = map(int, input().split())
        ans = -1
        for y in range(limitr - 400, limitr + 1):
            if not (limitl <= y <= limitr): continue
            for x in range(limitl, limitl + 400):
                if not (limitl <= x <= limitr): continue
                if math.gcd(x, y) != 1: continue
                ans = max(ans, abs(y - x))

        print(ans)

    # 1 time
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
        input = """2 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """14 21"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 100"""
        output = """99"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()