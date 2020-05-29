import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    def solve(n):
        a, b = 2, 0
        res = 0
        if n < 2:
            return [False, 0, 0]
        while True:
            if n >= (a+b):
                res += 1
                n -= (a+b)
            else:
                break;
            a += 2
            b += 1
        return [True, n, res]

    q = int(input())
    for _ in range(q):
        n = int(input())
        res = 0
        while True:
            a,b,c = solve(n)
            if a is True:
                res += 1
            else:
                break
            n = b
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
        input = """1
9"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()