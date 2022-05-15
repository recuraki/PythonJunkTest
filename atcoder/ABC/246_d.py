
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')
    def do():
        n = int(input())

        candidate = []
        ma = 10 ** 6 + 10
        ans = 10**100
        for a in range(ma):
            ng = -1
            ok = 10**6+10

            def f(b):
                val = a ** 3 + b ** 3 + a ** 2 * b + a * b ** 2
                if val >= n:
                    return True
                else:
                    return False

            def fv(b):
                return a ** 3 + b ** 3 + a ** 2 * b + a * b ** 2

            while (abs(ok - ng) > 1):
                mid = (ok + ng) // 2
                if (f(mid)):
                    ok = mid;
                else:
                    ng = mid;
            ans = min(ans, fv(ok))
        print(ans)
    # 1 time
    do()
    # n questions
    #q = int(input())
    #for _ in range(q):
    #    do()


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
        input = """9"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """999999999989449206"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()