import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


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
1 2 1
1 3 3"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 5 2
2 3 2
1 5 1
4 5 13"""
        output = """62"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
5 7 459221860242673109
6 8 248001948488076933
3 5 371922579800289138
2 5 773108338386747788
6 10 181747352791505823
1 3 803225386673329326
7 8 139939802736535485
9 10 657980865814127926
2 4 146378247587539124"""
        output = """241240228"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()