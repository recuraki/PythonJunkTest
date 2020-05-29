import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    n = int(input())
    dat = list(map(int, input().split()))
    s = [0] * (n+1)
    for i in range(n):
        s[i+1] = s[i] + dat[i];

    resval = -999999999999999999999
    res = 0

    for i in range(n):
        vmin = dat[i]
        for j in range(i+1, n):
            v = s[j+1] - s[i]
            vmin = max(vmin, dat[j])
            tmp = v - vmin
            resval = max(resval, tmp)
            #print(i, j, v, vmin, tmp)
    if resval < 0:
        print(0)
    else:
        print(resval)





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
5 -2 10 -1 4"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """8
5 2 5 3 -30 -30 6 9"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
-10 6 -15"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()