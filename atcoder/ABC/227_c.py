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
        ans = 0
        n = int(input())
        bmax = math.floor(math.sqrt(n))
        for b in range(bmax, 0, -1):
            cmax = n // b


        print(ans)
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
        input = """4"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """100"""
        output = """323"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100000000000"""
        output = """5745290566750"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()