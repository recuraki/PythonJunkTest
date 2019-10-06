import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat_x = list(map(int, input().split()))

    dat_x.sort()
    dat_x = list(map(lambda x: x + (1-dat_x[0]), dat_x))

    if m == 1:
        print(0)
    elif(n == m):
        print(0)
    else:
        distance = [0] * (m)
        for i in range(m - 1):
            distance[i] = dat_x[i+1] - dat_x[i]
        distance.sort(reverse=True)
        distance = distance[n - 1:]
        print(sum(distance))


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
        input = """2 5
10 12 1 2 14"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 7
-10 -3 0 9 -100 2 17"""
        output = """19"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """100 1
-100000"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()