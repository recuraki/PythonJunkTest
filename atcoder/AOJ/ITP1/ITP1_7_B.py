import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    while True:
        n, x = map(int, input().split())
        if n == x == 0:
            break
        res = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if a == b:
                    continue
                c = x - a - b
                if c!=a and c!= b and b<c<=n:
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
    def test_input_1(self):
        print("test_input_1")
        input = """5 9
0 0"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()