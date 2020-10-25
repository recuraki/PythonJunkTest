import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    n = int(input())
    x = n // 2
    res = 1
    for i in range(1,n+1):
        res *= i
    res //= x
    res //= x
    res //= 2
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
        input = """2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8"""
        output = """1260"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """20"""
        output = """12164510040883200"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()