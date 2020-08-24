import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    buf = []
    for i in range(n):
        l = max(0,   i - dat[i] - k)
        r = min(n-1, i + dat[i] + k)
        buf.append([l, r] )
    print(buf)
    light = [0] * n
    for i in range(n):
        l, r = buf[i]
        light[l] += 1
        light[r] -= 1
    print(light)




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
        input = """5 1
1 0 0 1 0"""
        output = """1 2 2 1 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2
1 0 0 1 0"""
        output = """3 3 4 4 3"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 2
5 0 0 0 0"""
        output = """5 4 5 4 5"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()