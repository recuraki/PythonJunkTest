import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))


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
2 3 2"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
158260522 877914575 602436426 24979445 861648772 623690081 433933447 476190629 262703497 211047202"""
        output = """524691026"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()