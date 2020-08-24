import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    import math
    def do():
        l, r, m = map(int, input().split())
        if l == r:
            print(ll,ll,ll)
            return

        for delta in [-1, 0, 1, 2, -1]:
            ll, rr = l, r
            cnt = 0
            while ll <= rr:
                cnt += 1
                mid = (rr+ll) // 2
                if cnt > 10:
                    break
                a = mid
                n = math.floor(m / a) + delta
                if n == 0:
                    rr = mid - 1
                    continue
                diff = n*a - m
                if abs(diff) > (r-l):
                    if diff < 0:
                        ll = mid + 1
                    else:
                        rr = mid - 1
                    continue

                # pat1
                b = r
                c = (n*a) + b - m
                if l <= a <= r and l<=b<=r and l<=c<=r and (m == n*a + b - c) and n > 0:
                    print(a, b, c)
                    return

                b = l
                c = (n*a) + b - m
                if l <= a <= r and l<=b<=r and l<=c<=r and (m==n*a+b-c) and n > 0:
                    print(a,b,c)
                    return




    q = int(input())
    for _ in range(q):
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
4 6 13
2 3 1"""
        output = """4 6 5
2 2 3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """1
4 4 4
"""
        output = """4 6 5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()