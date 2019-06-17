import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = 0
    dat_r = []
    for i in range(n):
        dat_r.append(int(input()))
    dat_r.sort(reverse=True)
    for i in range(n):
        r = dat_r[i]
        s += r*r if i%2==0 else -(r*r)
    import math
    print(s* math.pi)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """3
1
2
3"""
        output = """18.8495559215"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """6
15
2
3
7
6
9"""
        output = """508.938009881546"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()