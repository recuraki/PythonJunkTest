import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    t = int(input())
    for _ in range(t):
        n = int(input())
        dat = list(map(int, input().split()))
        dat.sort(reverse=True)
        print(" ".join(list(map(str, dat))))



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
1
7
4
1 1 3 5
6
3 2 1 5 6 4"""
        output = """7
1 5 1 3
2 4 6 1 3 5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()