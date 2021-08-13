import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n1, n2, n3 = map(int, input().split())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        dat3 = list(map(int, input().split()))

    q = int(input())
    for _ in range(q):
        do()
    # do()




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
        input = """2 4 1
1 2
6 3 4 5
5"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 2 2
7 5 4
2 9
7 1"""
        output = """29"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()