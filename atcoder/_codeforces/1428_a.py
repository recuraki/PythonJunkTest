
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        import math
        q = int(input())
        for _ in range(q):
            x1,y1,x2,y2 = map(int, input().split())
            if x1 == x2:
                print(abs(y1-y2))
                continue
            if y1 == y2:
                print(abs(x1 - x2))
                continue
            res = abs(y1-y2) + 2 + abs(x1 - x2)
            print(res)
            continue
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
        input = """2
1 2 2 2
1 1 2 2"""
        output = """1
4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()