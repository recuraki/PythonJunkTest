import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    import collections
    import bisect
    n = int(input())
    dat = list(map(int, input().split()))
    s = 0
    d = collections.defaultdict(list)
    dats = []
    dats.append(0)
    for i in range(n):
        s += dat[i]
        dats.append(s)
        d[s].append(i)
    print(dats)
    res = 0
    print(d)
    for i in range(n):
        cur = dats[i]
        print("i", i, "cur", cur)
        if dat[i] != 0:
            res += 1
        res += n - i - 1
        print(" > add", n - i - 1)
        print(" > search", cur)
        ind = bisect.bisect_right(d[cur], i+1)
        print(" > ind", ind)
        rest = len(d[cur]) - ind
        print(" > add reduce", rest)
        res -= rest
    if sum(dat) != 1:
        res -= 1
    print(res)




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_0(self):
        print("test_input_1")
        input = """7
1 2 4 8 -4 -4 -4"""
        output = """14"""
        self.assertIO(input, output)

    def test_input_00(self):
        print("test_input_1")
        input = """10
0 0 0 1 2 3 -3 -2 -1 0 0 0"""
        output = """14"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_1")
        input = """3
1 2 -3"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
41 -41 41"""
        output = """3"""
        self.assertIO(input, output)




if __name__ == "__main__":
    unittest.main()