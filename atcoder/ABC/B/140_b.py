import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = map(int, input().split())
    dat_b = map(int, input().split())
    dat_c = map(int, input().split())
    dat_a = list(dat_a)
    dat_b = list(dat_b)
    dat_c = list(dat_c)
    last = -100
    res = 0
    for i in range(n):
        a = dat_a[i] - 1
        res += dat_b[a]
        if last == (a - 1):
            res += dat_c[last]
        last = a
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
    def test_input_1(self):
        print("test_input_1")
        input = """3
3 1 2
2 5 4
3 6"""
        output = """14"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
2 3 4 1
13 5 8 24
45 9 15"""
        output = """74"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
1 2
50 50
50"""
        output = """150"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()