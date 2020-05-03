import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    q = int(input())
    for _ in range(q):
        n = int(input())
        if n == 2:
            print(2)
        else:
            a = "1"
            b = "0"
            for i in range(n//2):
                a += "0"
                b += "1"
            for i in range(n//2 - 1):
                a += "1"
                b += "0"
            a += "0"
            b += "0"
            a = int(a, 2)
            b = int(b, 2)
            print(abs(a-b))



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
2
4
6
8"""
        output = """2
6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()