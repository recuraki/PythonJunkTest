import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    for i in range(k):
        s = str(n)
        s1 = "".join(sorted(list(s), reverse=True))
        s2 = "".join(sorted(list(s)))
        n = int(s1) - int(s2)
    print(n)


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
        input = """314 2"""
        output = """693"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000000 100"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6174 100000"""
        output = """6174"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """111 100000"""
        output = """0"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()