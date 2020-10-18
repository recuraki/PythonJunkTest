import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c,d = map(int, input().split())
    if a+b == c+d:
        print("Yes")
    elif a + c == b + d:
        print("Yes")
    elif a+d == b+c:
        print("Yes")
    elif b+c == a+d:
        print("Yes")
    elif b+d == a+c:
        print("Yes")
    elif c+d == a+b:
        print("Yes")
    elif a == b + c + d:
        print("Yes")
    elif b == a + c + d:
        print("Yes")
    elif c == a + b + d:
        print("Yes")
    elif d == a + b + c:
        print("Yes")
    else:
        print("No")



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
        input = """1 3 2 4"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 2 4 8"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()