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
    import bisect
    for _ in range(q):
        n = int(input())
        data = list(map(int, input().split()))
        datb = list(map(int, input().split()))
        datc = []
        indmin = []
        indplus = []
        for i in range(n):
            if data[i] == 1:
                indplus.append(i)
            elif data[i] == -1:
                indmin.append(i)
        f = True
        for i in range(n-1, -1, -1):
            d = datb[i] - data[i]
            if d == 0:
                continue
            elif d > 0:
                ind = bisect.bisect_left(indplus, i)
                if ind == 0:
                    f = False
            elif d < 0:
                ind = bisect.bisect_left(indmin, i)
                if ind == 0:
                    f = False
        print("YES" if f  else "NO")





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
        input = """5
3
1 -1 0
1 1 -2
3
0 1 1
0 2 2
2
1 0
1 41
2
-1 0
-1 -41
5
0 1 -1 1 -1
1 1 -1 1 -1"""
        output = """YES
NO
YES
YES
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()