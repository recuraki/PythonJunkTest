import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat = []
    hq = []
    for i in range(k):
        dat.append( 0 ) # count
        hq.append( (0, i) ) # count, index
    import heapq
    heapq.heapify(hq)

    for _ in range(n):
        c = int(input())
        cindex = c % k
        dat[cindex] += 1
        x = heapq.heappop()


        print(r[1] * k + r[0])




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
0
1
2
2
0
0
10"""
        output = """1
2
3
3
4
4
7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
1
2
1
2"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()