import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        v, a, b, c = map(int, input().split())
        dat = [a, b, c]
        ans = ["F", "M", "T"]
        i = 0
        while v > 0:
            if v >= dat[i]:
                v -= dat[i]
            else:
                break
            i += 1
            i %= 3
        print(ans[i])

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
        input = """25 10 11 12"""
        output = """T"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """30 10 10 10"""
        output = """F"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000 1 1 1"""
        output = """M"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()