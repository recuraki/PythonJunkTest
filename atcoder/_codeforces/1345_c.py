import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    import collections
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))

        used = dict()

        res = list(range(0, n))
        can = True
        for j in range(len(res)):
            v = res[j] + dat[res[j] % n]
            v %= n
            if v in used:
                can = False
                break
            used[v] = True
        print("YES" if can else "NO")

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
        input = """6
1
14
2
1 -1
4
5 5 5 1
3
3 2 1
2
0 1
5
-239 -2 -100 -3 -11"""
        output = """YES
YES
YES
NO
NO
YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()