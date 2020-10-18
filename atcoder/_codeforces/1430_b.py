import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        q = int(input())
        for _ in range(q):
            n, k = map(int, input().split())
            dat = list(map(int, input().split()))
            dat.sort(reverse=True)
            print(sum(dat[:k+1]))

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
        input = """4
4 1
5 5 5 5
3 2
0 0 0
4 1
1 3 2 4
4 2
1 3 2 4"""
        output = """10
0
7
9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()