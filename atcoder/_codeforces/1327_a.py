import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(n, d=2, a=1):
        return int(n / 2 * (2 * a + (n - 1) * d))

    from pprint import pprint
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        f = True
        t = do(k)
        #print(n, t)
        if n == t:
            pass
        elif n < t:
            f = False
        elif (n-t) % 2 == 0:
            pass
        else:
            f = False

        print("YES" if f else "NO")

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
        input = """6
3 1
4 2
10 3
10 2
16 4
16 5"""
        output = """YES
YES
NO
YES
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()