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

    def do():
        n = int(input())
        import math
        ans2 = 0
        l = 1
        cnt = 0
        while True:
            cnt += 1
            val = math.floor(n / l)
            if val == 0: break
            r = math.floor(n / val)
            x = val * (r - l + 1)
            ans2 += x
            l = r + 1
        print(ans2)


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
        input = """3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10000000000"""
        output = """231802823220"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()