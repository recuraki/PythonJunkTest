import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    from pprint import pprint

    INF = 1 << 63
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = []
        for i in range(n):
            buf.append( (dat[i], i + 1) )
        buf.sort(reverse=True)
        print(buf[1][1])

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
        input = """6
1 123 12345 12 1234 123456"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 1 4 15 9"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()