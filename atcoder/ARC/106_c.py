import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        n, m = map(int, input().split())
        if m == 0:
            for i in range(n):
                x = i+1
                print(10*x, 10*x+1)
            return
        if n == abs(m) or n-1 == abs(m) or m < 0: # caonnot
            print(-1)
            return
        if m > 0: # can
            print(1, 10**7)
            for i in range(m + 1):
                x = i+1
                print(10*x, 10*x+1)
            for i in range(n - m - 2):
                x = i+1
                print(10**7 + 10*x, 10**7 + 10*x+1)
            return
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

    def test_input_11(self):
        print("test_input_11")
        input = """5 4"""
        output = """"""
        self.assertIO(input, output)

    def test_input_1(self):
        return True
        print("test_input_1")
        input = """5 1"""
        output = """1 10
8 12
13 20
11 14
2 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 -10"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 0"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()