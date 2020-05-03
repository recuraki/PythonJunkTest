import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    used = [False] * 200100
    #print(n,m)
    for i in range(1, m+1):
        for j in range(n):
            if used[j] is False and used[(j+i) % n] is False:
                print(j+1, j+i+1)
                used[j] = True
                used[(j + i) % n] = True
                break





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
        input = """4 1"""
        output = """2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 3"""
        output = """1 6
2 5
3 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()