import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = map(int, input().split())
    dat_a = list(dat_a)
    bug = 0
    n = 0
    for i in range(len(dat_a)):
        if dat_a[i] != 0:
            n += 1
            bug += dat_a[i]
    import math
    print(math.ceil(bug/n))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """4
0 1 3 8"""
        output = """4"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """5
1 4 9 10 15"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()