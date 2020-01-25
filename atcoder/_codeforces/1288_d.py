import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())

    dat = []
    sss = []
    for i in range(10):
        sss.append([])

    for i in range(n):
        dat.append(list(map(int, input().split())))
        for j in range(m):
            sss[j].append(dat[i][j])
    for j in range(m):
        sss[j] = list(set(sss[j]))
        sss[j].sort()
    r = []
    import bisect
    for i in range(n):
        tl = []
        for j in range(m):
            t = bisect.bisect_right(sss[j], dat[i][j])
            tl.append(t)

        r.append(tl)
    res = []
    for i in range(n):
        res.append( (sum(r[i]), i))
    res.sort(reverse=True)
    print("{0} {1}".format(res[1][1], res[0][1]))

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
        input = """6 5
5 0 3 1 2
1 8 9 1 3
1 2 3 4 5
9 1 0 3 7
2 3 0 6 3
6 4 1 7 0"""
        output = """1 5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()