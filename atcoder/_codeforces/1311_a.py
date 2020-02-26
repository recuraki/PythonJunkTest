import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        if a == b:
            print(0)
        elif a > b:
            if a%2 == 1 and b%2 == 0:
                print(2)
            elif a%2 == 1 and b%2 == 1:
                print(1)
            elif a%2 == 0 and b%2 == 0:
                print(1)
            elif a%2 == 0 and b%2 == 1:
                print(2)
        else: # a < b
            if a%2 == 1 and b%2 == 0:
                print(1)
            elif a%2 == 1 and b%2 == 1:
                print(2)
            elif a%2 == 0 and b%2 == 0:
                print(2)
            elif a%2 == 0 and b%2 == 1:
                print(1)






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
        input = """5
2 3
10 10
2 4
7 4
9 3"""
        output = """1
0
2
2
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()