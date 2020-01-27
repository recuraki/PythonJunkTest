import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def dp(s):
        if True:
            print(s)

    def dpp(s):
        if True:
            pprint(s)

    n, q = map(int, input().split())
    l = [0] * n
    for _ in range(q):
        qq = input().split()
        if qq[0] == "0":
            x, y ,z = qq[1],qq[2],qq[3]
            x = int(x)
            y=int(y)
            z = int(z)
            l[y] = l[x] + z
        if qq[0] == "1":
            x, y = qq[1],qq[2]
            x = int(x)
            y=int(y)
            print(l[y] - l[x])



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
        input = """5 6
0 0 2 5
0 1 2 3
1 0 1
1 1 3
0 1 4 8
1 0 4"""
        output = """2
?
10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()