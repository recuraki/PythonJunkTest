import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        from fractions import Fraction
        n = int(input())
        res = 0
        for i in range(10, 0, -1):
            x = 1
            for j in range(1, i + 1):
                x *= j
            #print(x)
            res += n // x
            n = n % x
        print(res)

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
        input = """9"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """119"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10000000"""
        output = """24"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()