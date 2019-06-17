import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        x = dat_a[i]
        while x%2 == 0 or x%3 ==2:
            x -= 1
            res += 1
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
    def test_input1(self):
        print("test_input1")
        input = """3
5 8 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """9
1 2 3 4 5 6 7 8 9"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()