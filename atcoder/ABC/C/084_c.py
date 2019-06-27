import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat_b = list(map(int, input().split()))
    dat_c = list(map(int, input().split()))
    dat_a.sort()
    dat_b.sort()
    dat_c.sort()

    print(n)
    import bisect
    res = 0
    for i in range(n):
        x = bisect.bisect_left(dat_b, dat_a[i])
        if x == n:
            print("!!!")
            break
        print("dat_bx = {0}".format(dat_b[x]))

        y = bisect.bisect_left(dat_c, dat_b[x])
        if y == n:
            break
        print("y = {0}".format(y))

        print("x,y = {0} {1}".format(x,y))
        res += (n-x) * (n-y)

    print(res)

"""
3 14 159
1 9 58 79
1 2 50 79
"""


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
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288"""
        output = """87"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()