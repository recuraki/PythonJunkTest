import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    buf = [0] * (10**5 + 100)
    res = 0
    for i in range(n):
        buf[dat[i]] += 1
        res += dat[i]
    q = int(input())
    for _ in range(q):
        b, c = map(int, input().split())
        res -= b * buf[b]
        res += c * buf[b]
        buf[c] += buf[b]
        buf[b] = 0
        print(res)

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
1 2 3 4
3
1 2
3 4
2 4"""
        output = """11
12
16"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1 1 1
3
1 2
2 1
3 5"""
        output = """8
4
4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
1 2
3
1 100
2 100
100 1000"""
        output = """102
200
2000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()