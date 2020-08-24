import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b, x, n = map(int, input().split())
    if x == 1 or b == 1:
        if a >= n:
            print("YES")
        else:
            print("NO")
    elif b == 0:
        a = 0
        if a >= n:
            print("YES")
        else:
            print("NO")
    elif a == 0:
        if a >= n:
            print("YES")
        else:
            print("NO")
    else:
        can = False
        if a >= n:
            can = True
        for i in range(x-1):
            a *= b
            #print("i", i, a)
            if a >= n:
                can = True
                break
            if a > 10**18:
                break
        print("YES" if can else "NO")





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
        input = """1 2 3 4"""
        output = """YES"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 3 3 333"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_23(self):
        print("test_input_23")
        input = """100 100 3 303350"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()