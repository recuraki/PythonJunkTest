import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    qq = int(input())
    for _ in range(qq):
        n = int(input())
        dat = list(map(int, input().split()))
        if n == 1:
            print("YES")
            continue
        c = dat[0] % 2
        f = True
        for i in range(n):
            if c != dat[i] % 2:
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
        input = """4
3
1 1 3
4
1 1 2 1
2
11 11
1
100"""
        output = """YES
NO
YES
YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()