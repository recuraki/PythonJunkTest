import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    q = int(input())
    for qq in range(q):
        n, d = map(int, input().split())
        a, b = None, None
        try:
            a = (n-1) + math.sqrt( (n-1) * (n-1) - 4*(d-n) )
        except ValueError:
            pass
        try:
            b = (n-1) - math.sqrt( (n-1) * (n-1) - 4*(d-n))
        except ValueError:
            pass
        if a is not None or b is not None:
            print("YES")
        else:
            print("NO")



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
1 1
3 5
3 6"""
        output = """YES
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()