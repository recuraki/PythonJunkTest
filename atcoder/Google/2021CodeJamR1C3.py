import sys
from io import StringIO
import unittest
import logging

logging.basicConfig(level=logging.DEBUG)


def resolve():
    def do(taskno):
        s, t = input().split()
        s = int(s, 2)
        t = int(t, 2)
        if s == t:
            res = 0
            print("Case #{0}: {1}".format(taskno, res))
            return
        res = 10**9
        loop = 9
        for pat in range(2 ** loop):
            x = s
            for i in range(loop):
                if ((pat >> i) & 1) == 0: #not
                    large = 0
                    debugcnt = 0
                    if x == 0:
                        large = 1
                    else:
                        while x >= (2**large):
                            large += 1
                    x = (2**large - 1) ^ x
                else: # bit shift
                    x <<= 1
                if x == t:
                    res = min(res, i+1)
        if res == 10**9:
            res = "IMPOSSIBLE"
        print("Case #{0}: {1}".format(taskno, res))
    q = int(input())
    for qq in range(q):
        do(qq + 1)


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
10001 111
1011 111
1010 1011
0 1
0 101
1101011 1101011"""
        output = """Case #1: 4
Case #2: 3
Case #3: 2
Case #4: 1
Case #5: IMPOSSIBLE
Case #6: 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()