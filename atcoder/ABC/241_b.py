import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    datb = list(map(int, input().split()))
    data.sort()
    datb.sort()
    i = j = 0
    while i < n and j < m:
        if data[i] == datb[j]:
            i, j = i+1, j+1
            continue
        if data[i] > datb[j]: break
        i += 1
    if j == m: print("Yes")
    else: print("No")





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
        input = """3 2
1 1 3
3 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1
1000000000
1"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 2
1 2 3 4 5
5 5"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()