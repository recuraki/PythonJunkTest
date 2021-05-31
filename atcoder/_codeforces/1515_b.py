import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    issqrt = set()
    for i in range(1, 100000):
        issqrt.add(i**2)
    def do():
        n = int(input())
        if n % 2 == 1:
            print("NO")
            return
        while n % 2 == 0:
            n //= 2
        if n in issqrt:
            print("YES")
        else:
            print("NO")
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
        input = """3
2
4
6"""
        output = """YES
YES
NO"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1
18
"""
        output= ""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()