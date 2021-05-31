import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    import sys
    #input = sys.stdin.readline
    from pprint import pprint


    def do():
        def sigma1(n):
            return n * (n + 1) // 2
        x, y, k = map(int, input().split())
        cost =  (x - 1) + x * (y-1)
        print("YES" if cost == k else "NO")



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
        input = """6
1 1 0
2 2 2
2 2 3
2 2 4
1 4 3
100 100 10000"""
        output = """YES
NO
YES
NO
YES
NO"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
4 3 0"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()