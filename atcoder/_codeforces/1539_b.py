import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

"""
TLEのポイント:
- 入力高速化(*dat)
REの時のポイント
- inputしきっていますか？

"""

def resolve():
    class cumSum1D(object):
        sdat = []

        def init(self):
            pass

        def load(self, l):
            import itertools
            self.sdat = list(itertools.accumulate(itertools.chain([0], l)))

        def query(self, l, r):
            """
            query [l, r)
            """
            # assert l < r
            return self.sdat[r] - self.sdat[l]

    import sys
    input = sys.stdin.readline
    from pprint import pprint
    def do():
        n, q = map(int, input().split())
        s = input()
        l = [0] * n
        for i in range(n):
            l[i] = ord(s[i]) - ord("a") + 1
        st = cumSum1D()
        st.load(l)
        for _ in range(q):
            l, r = map(int, input().split())
            l-=1
            r-=1
            print(st.query(l, r+1))

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
        input = """7 3
abacaba
1 3
2 5
1 7"""
        output = """4
7
11"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 4
abbabaa
1 3
5 7
6 6
2 4"""
        output = """5
4
1
5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """13 7
sonoshikumiwo
1 5
2 10
7 7
1 13
4 8
2 5
3 9"""
        output = """82
125
9
191
62
63
97"""
        self.assertIO(input
                      , output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()