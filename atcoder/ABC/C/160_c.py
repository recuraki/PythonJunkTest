import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k, n = map(int, input().split())
    dat = list(map(int, input().split()))
    d = []
    c = dat[0]
    for i in range(n):
        d.append(dat[i] - c)
        c = dat[i]
    d.append(k - dat[-1] + dat[0])
    d.sort(reverse=True)
    #print(d)
    print(sum(d[1:]))


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
        input = """20 3
5 10 15"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20 3
0 5 15"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """18 3
3 7 12"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()