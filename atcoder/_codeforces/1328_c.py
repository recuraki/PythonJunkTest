import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        s = input()
        a = ["0"] * n
        b = ["0"] * n
        a[0] = "1"
        b[0] = "1"
        islock = False
        for i in range(1, n):
            if islock:
                b[i] = s[i]
                continue
            if s[i] == "2":
                a[i] = "1"
                b[i] = "1"
                continue
            if s[i] == "0":
                a[i] = "0"
                b[i] = "0"
                continue
            if s[i] == "1":
                a[i] = "1"
                b[i] = "0"
                islock = True
        print("".join(a))
        print("".join(b))





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
5
22222
5
21211
1
2
9
220222021"""
        output = """11111
11111
11000
10211
1
1
110111011
110111010"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()