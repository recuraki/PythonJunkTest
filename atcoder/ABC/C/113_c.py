import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat = []
    res = []
    for i in range(m):
        res.append(None)

    for i in range(m):
        p, y = map(int, input().split())
        dat.append( ( i,p,y ))

    dat.sort(key=lambda x: x[2])

    city = [1] * (n + 1)
    for i in range(m):
        (i, c, y) = dat[i]
        r = city[c]
        city[c] += 1
        res[i] = "%06d%06d" % (c, r)

    for i in range(m):
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
        input = """2 3
1 32
2 63
1 12"""
        output = """000001000002
000002000001
000001000001"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 3
2 55
2 77
2 99"""
        output = """000002000001
000002000002
000002000003"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()