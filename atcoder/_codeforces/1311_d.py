import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(a, b, c):
        f = False
        for x in range(1000):
            for i in range(x):
                for j in range(x - i):
                    for k in range(x - i - j):
                        if (c - k) % (b - j) == 0 and (b - j) % (a - i) == 0:
                            if a-i > 0 and b-j > 0 and c-k > 0:
                                ra, rb, rc = a - i, b - j, c - k
                                f = True
                        if (c + k) % (b - j) == 0 and (b - j) % (a - i) == 0:
                            if a-i > 0 and b-j > 0 :
                                ra, rb, rc = a - i, b - j, c + k
                                f = True
                        if (c - k) % (b + j) == 0 and (b + j) % (a - i) == 0:
                            if a-i > 0 and c-k > 0:
                                ra, rb, rc = a - i, b + j, c - k
                                f = True
                        if (c + k) % (b + j) == 0 and (b + j) % (a - i) == 0:
                            if a-i > 0 :
                                ra, rb, rc = a - i, b + j, c + k
                                f = True
                        if (c - k) % (b - j) == 0 and (b - j) % (a + i) == 0:
                            if b-j > 0 and c-k > 0:
                                ra, rb, rc = a + i, b - j, c - k
                                f = True
                        if (c - k) % (b + j) == 0 and (b + j) % (a + i) == 0:
                            if c-k > 0:
                                ra, rb, rc = a + i, b + j, c - k
                                f = True
                        if (c + k) % (b + j) == 0 and (b + j) % (a + i) == 0:
                            ra, rb, rc = a + i, b + j, c + k
                            f = True
                        if (c + k) % (b - j) == 0 and (b - j) % (a + i) == 0:
                            if b-j > 0 :
                                ra, rb, rc = a + i, b - j, c + k
                                f = True

                    if f:
                        break
                if f:
                    break
            if f:
                break

        return ra, rb, rc

    from pprint import pprint
    qq = int(input())
    print()
    for _ in range(qq):
        a,b,c = map(int, input().split())
        na,nb,nc = do(a,b,c)
        cost = abs(na-a) + abs(nb-b) + abs(nc-c)
        print(cost)
        print(na,nb,nc)


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
        input = """8
1 1 1
123 321 456
5 10 15
15 18 21
100 100 101
1 22 29
3 19 38
6 30 46"""
        output = """0
1 1 1
102
114 228 456
4
4 8 16
6
18 18 18
1
100 100 100
7
1 22 22
2
1 19 38
8
6 24 48"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()