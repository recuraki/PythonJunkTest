import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        class Bit:
            def __init__(self, n):
                self.size = n
                self.tree = [0] * (n + 1)

            def sum(self, i):
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & -i
                return s

            def add(self, i, x):
                while i <= self.size:
                    self.tree[i] += x
                    i += i & -i

        class RangeUpdate:
            def __init__(self, n):
                self.p = Bit(n + 1)
                self.q = Bit(n + 1)

            def add(self, s, t, x):
                t += 1
                self.p.add(s, -x * s)
                self.p.add(t, x * t)
                self.q.add(s, x)
                self.q.add(t, -x)

            def sum(self, s, t):
                t += 1
                return self.p.sum(t) + self.q.sum(t) * t - \
                       self.p.sum(s) - self.q.sum(s) * s


        n = int(input())
        bit = RangeUpdate(200000 + 10)
        for _ in range(n):
            l, r = map(int, input().split())
            bit.add(l, r-1, 1)
        ans = []
        l = None
        for i in range(200000 + 10):
            if bit.sum(i, i) > 0:
                if l == None:
                    l = i
                else:
                    continue
            else: # = 0
                if l == None:
                    continue
                else:
                    ans.append((l, i))
                    l = None
        for x in ans:
            print(*x)
    # 1 time
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
10 20
20 30
40 50"""
        output = """10 30
40 50"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
10 40
30 60
20 50"""
        output = """10 60"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_")
        input = """2
1 2
2 3"""
        output = """1 3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()