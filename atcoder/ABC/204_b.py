import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        res = 0
        for x in dat:
            if x <= 10:
                continue
            res += x - 10
        print(res)

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
6 17 28"""
        output = """25"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
8 9 10 11"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()