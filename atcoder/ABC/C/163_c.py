import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat.reverse()
    count = [0] * (n + 1)
    for i in range(n - 1):
        count[dat[i]] += 1
    #print(count)
    res = count[1:]
    for i in range(len(res)):
        print(res[i])

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
1 1 2 2"""
        output = """2
2
0
0
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1 1 1 1 1 1 1 1 1"""
        output = """9
0
0
0
0
0
0
0
0
0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
1 2 3 4 5 6"""
        output = """1
1
1
1
1
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()