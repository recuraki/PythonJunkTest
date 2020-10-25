import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        q = int(input())
        for _ in range(q):
            a,b = map(int, input().split())
            x = a^b
            print(x)
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
6 12
4 9
59 832
28 14
4925 2912
1 1"""
        output = """10
13
891
18
6237
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()