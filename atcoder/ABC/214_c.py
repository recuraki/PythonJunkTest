import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
        n = int(input())
        dats = list(map(int, input().split()))
        datt = list(map(int, input().split()))
        res = [INF] * n
        startval = min(datt)
        startind = datt.index(startval)
        res[startind] = startval
        for i in range(startind, n+n+n):
            res[(i + 1) % n] = min(res[(i + 1) % n], datt[(i + 1) % n])
            res[(i + 1) % n] = min(res[(i + 1) % n], res[i % n] + dats[i % n])
        for x in res:
            print(x)
    do()





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
        input = """3
4 1 5
3 10 100"""
        output = """3
7
8"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
100 100 100 100
1 1 1 1"""
        output = """1
1
1
1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
1 2 3 4
1 2 4 7"""
        output = """1
2
4
7"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """8
84 87 78 16 94 36 87 93
50 22 63 28 91 60 64 27"""
        output = """50
22
63
28
44
60
64
27"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()