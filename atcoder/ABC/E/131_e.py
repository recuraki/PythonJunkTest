import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat = []
    for i in range(n):
        dat.append( (i + 1), (i + 2) )
    cur = (n - 1) * (n - 2) // 2
    if k > cur:
        print(-1)
    else:
        for i in range(cur - k):
            dat.append()




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
        input = """5 3"""
        output = """5
4 3
1 2
3 1
4 5
2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 8"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()