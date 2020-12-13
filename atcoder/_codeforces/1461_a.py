import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        s = "abc"* 1000
        n, k = map(int, input().split())
        print(s[:n])
        print(len(s[:n]))

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
        input = """2
1000 2
4 1"""
        output = """aab
acba"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()