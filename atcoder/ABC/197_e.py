import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    pass

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
        input = """5
2 2
3 1
1 3
4 2
5 3"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9
5 5
-4 4
4 3
6 3
-5 5
-3 2
2 2
3 3
1 4"""
        output = """38"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()