import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #input = sys.stdin.readline
    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]

    from pprint import pprint
    import sys
    import collections
    input = sys.stdin.readline

    import heapq

    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort()
    l = countstrs(dat)
    buf = []
    for i in range(len(l)):
        a,b = l[i]
        buf.append([-b, a])
    print(buf)

    heapq.heapify(buf)

    hakobudict = collections.defaultdict(int)
    needs = [4,2,2]
    q = int(input())
    for _ in range(q):
        a, b = input().split()
        b = int(b)
        if a == "+":
            hakobudict[-b] += 1
        else:
            hakobudict[-b] -= 1
        tmpbuf = []
        can = True
        made = [False] * len(needs)
        curnum = 0
        for i in range(len(needs)):
            if len(buf) == 0:
                break
            curnum, nagasa = heapq.heappop(a)

            if curnum == 1:
                break










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
1 1 1 2 1 1
6
+ 2
+ 1
- 1
+ 2
- 1
+ 2"""
        output = """NO
YES
NO
NO
NO
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()