import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        a = int(input())
        b = int(input())
        c = b // 2
        d = 5 if (b % 2 == 1) else 0
        ans = str(c) + str(d) + "0" + str(a)
        print(int(ans))
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
        input = """13
62"""
        output = """131"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """69120
824"""
        output = """869120"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6283185
12566370"""
        output = """6283185"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """1
1"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()