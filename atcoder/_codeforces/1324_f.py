import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    v =[]
    for i in range(n+1):
        v.append([])
    score = [0] * (n)
    for i in range(n-1):
        a, b = map(int, input().split())
        v[a-1].append(b-1)
        v[b-1].append(a-1)
    for i in range(n):
        for x in v[i]:
            score[i] += 1





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
        input = """9
0 1 1 1 0 0 0 0 1
1 2
1 3
3 4
3 5
2 6
4 7
6 8
5 9"""
        output = """2 2 2 2 2 1 1 0 2 """
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()