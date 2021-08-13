import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def resolve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    res = max(a-c, a-d, b-c, b-d)
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
        input = """0 10
0 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """-100 -100
100 100"""
        output = """-200"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """-100 100
-100 100"""
        output = """200"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()