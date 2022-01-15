import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        n, m = map(int, input().split())
        g1 = [[False] * n for _ in range(n)]
        g2 = [[False] * n for _ in range(n)]
        dat = []
        for _ in range(m):
            a, b = map(lambda x: int(x) - 1, input().split())
            dat.append( (a, b) )
        for _ in range(m):
            a, b = map(lambda x: int(x) - 1, input().split())
            g2[a][b] = True
            g2[b][a] = True
        from itertools import permutations
        for mapping in permutations(list(range(n))):
            can = True
            for a, b in dat:
                c, d = mapping[a], mapping[b]
                if g2[c][d]: continue
                can = False
                break
            if can:
                print("Yes")
                return
        print("No")
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
        input = """4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 6
1 2
1 3
1 4
3 4
3 5
4 5
1 2
1 3
1 4
1 5
3 5
4 5"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8 0"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()