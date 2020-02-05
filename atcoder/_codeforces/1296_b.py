import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)

    q = int(input())
    for _ in range(q):
        s = int(input())
        res = 0
        while s > 9:
            sm = s % 10
            res += (s - s % 10)
            s = s // 10
            s += sm
            if s < 9:
                break

        res += s

        print(res)


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
        input = """6
1
10
19
9876
12345
1000000000"""
        output = """1
11
21
10973
13716
1111111111"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()