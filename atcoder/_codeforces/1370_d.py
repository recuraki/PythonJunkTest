import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    import collections
    import heapq
    import math
    oddq = []
    evenq = []
    heapq.heapify(oddq)
    heapq.heapify(evenq)
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))
    for i in range(len(dat)):
        v = dat[i]
        if i % 2 == 0:
            heapq.heappush(evenq, -v)
        else:
            heapq.heappush(oddq, -v)
    canerase = math.floor( (n - k) /2)
    print("canerase", canerase)

    res = 9999999999999999999999999999
    for i in range(canerase):
        if len(evenq) > 0:
            heapq.heappop(evenq)
    for i in range(canerase):
        if len(oddq) > 0:
            heapq.heappop(oddq)

    if len(evenq) > 0:
        val = 0 - heapq.heappop(evenq)
        res = min(res, val)
    if len(oddq) > 0:
        val = 0 - heapq.heappop(oddq)
        res = min(res, val)
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
    def test_input_1(self):
        print("test_input_1")
        input = """4 2
1 2 3 4"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1 2 3 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 3
5 3 4 2 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """6 4
5 3 50 2 4 5"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()