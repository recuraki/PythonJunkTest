import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        s = input()

        def do(s, k):
            s = s
            k = k
            l = len(s)
            c0 = c1 = 0
            d = []
            for i in range(l):
                if s[i] == "0":
                    c0 += 1
                else:
                    c1 += 1
                d.append(c0 - c1)

            last = d[-1]  # 最後の
            if s[0] == "0":
                c0 += 1
            else:
                c1 += 1
            first = d[0]
            nextfirst = c0 - c1


            mind = min(d)
            maxd = max(d)
            diffnext = nextfirst - d[0]
            loop = int(abs(((k - maxd) / diffnext) - ((k - mind) / diffnext))) + 1
            truek = int(k - (diffnext * ((k - maxd) / diffnext)))

            if diffnext == 0 and c0 - c1 != 0:
                return  -1

            k = 0
            res = 0
            c0 = c1 = 0
            for q in range(loop + 2):
                for i in range(len(s)):
                    if (c0 - c1) == truek:
                        res += 1
                    if s[i] == "0":
                        c0 += 1
                    else:
                        c1 += 1
            return res

        print(do(s,x))

import collections
d= collections.deque
d.appendleft()
"""

123456789
010010
"""

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
6 10
010010
5 3
10101
1 0
0
"""
        output = """3
0
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()