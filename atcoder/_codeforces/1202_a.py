
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    dat = map(int, input().split())
    dat = list(dat)
    dat.sort()
    a = dat[3] - dat[0]
    b = dat[3] - dat[1]
    c = dat[3] - dat[2]
    print("{0} {1} {2}".format(a,b,c))

class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """3 6 5 4"""
        output = """2 1 3"""
        self.assertIO(input, output)

        def test_input_2(self):
            print("test_input_2")
            input = """
            """
            output = """YES"""
            self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_2")
        input = """4D
AS AC AD AH 5H"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()