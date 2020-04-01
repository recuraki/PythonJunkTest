import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, l, r = map(int, input().split())

    l -= 1
    r -= 1

    dist = [0] * 10000000

    for a in range(n):
        for b in range(a+1, n):
            #print("from", a, "to", b)
            c = 9999999999
            c = min(c, b - a)
            #print(" dire", c)
            c = min(c, abs( abs(l - a) + abs(r - b) ) + 1 )
            dist[c] += 1
    for k in range(1, n):
        print(dist[k])





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
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()