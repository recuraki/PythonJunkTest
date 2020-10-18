import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    dat = list(map(int, input().split()))
    res = 0
    res2 = 0
    dat2 = []
    for i in range(n):
        res += abs(dat[i])
        res2 += abs(dat[i])*abs(dat[i])
        dat2.append(abs(dat[i]))
    print(res)
    print(math.sqrt(res2))
    print(max(dat2))



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
2 -1"""
        output = """3
2.236067977499790
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
3 -1 -4 1 -5 9 2 -6 5 -3"""
        output = """39
14.387494569938159
9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()