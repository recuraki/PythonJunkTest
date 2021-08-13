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
        import collections
        d = collections.defaultdict(int)
        for x in dat:
            d[x] += 1
        res = 0
        for x in dat:
            res += n - d[x]
        print(res//2)

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
1 7 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1 10 100 1000 10000 100000 1000000 10000000 100000000 1000000000"""
        output = """45"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4"""
        output = """173"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()