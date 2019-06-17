import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,m = map(int, input().split())
    dat_n = []
    dat_m = []
    for i in range(n):
        a,b = map(int, input().split())
        dat_n.append((a, b))
    for i in range(m):
        a,b = map(int, input().split())
        dat_m.append((a, b))
    for i in range(n):
        a, b = dat_n[i]
        index = -1
        distance = 1000000001
        for j in range(m):
            c,d = dat_m[j]
            t = abs(a-c) + abs(b-d)
            if t < distance:
                index = j + 1
                distance = t
        print(index)


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
        input = """2 2
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()