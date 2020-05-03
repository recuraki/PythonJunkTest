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
        d = dict()
        f = True
        lp = -1
        for _ in range(n):
            p, c = map(int, input().split())
            if lp > p:
                f = False
            if p in d:
                if d[p] != c:
                    f = False
            if p < c:
                f = False
            d[p] = c
            lp = p
        k = list(d.keys())
        k.sort()
        #print(k)
        c = 0
        for x in k:
            if d[x] < c:
                f = False
            c = d[x]
        print("YES" if f else "NO")



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
        input = """7
3
0 0
1 1
1 2
2
1 0
1000 3
4
10 1
15 2
10 2
15 2
1
765 432
2
4 4
4 3
5
0 0
1 0
1 0
1 0
1 0
2
1 1
0 1"""
        output = """NO
YES
NO
YES
NO
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()