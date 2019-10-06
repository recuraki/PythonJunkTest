import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c = map(int, input().split())
    d = sorted([a,b,c])
    if d[0] == d[2]:
        print("Yes")
    else:
        print("No")

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
        logging.info("test_input_1")
        input = """2 2 2"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """3 4 5"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()