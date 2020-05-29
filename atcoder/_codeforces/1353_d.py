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
    q = int(input())
    import heapq
    for _ in range(q):
        #print("----")
        n = int(input())
        res = [0] * (n + 10)
        h = [ (-n, 1, n) ]
        heapq.heapify(h)
        for i in range(n):
            #print("h", h)
            len, l, r = heapq.heappop(h)
            #print(" > fetch", -len, l, r)
            len = -len
            if (r-l+1) % 2 == 1:
                a = (l+r) // 2
            else:
                a = (l+r-1) // 2
            res[a] = (i + 1)
            #print(" in> ", a, i+1)
            if (a - 1 >= l):
                heapq.heappush(h, [-(a - l  ) ,l, a - 1])
                #print(" > push",  [-(a - l  ) ,l, a - 1])
            if (a + 1 <= r):
                heapq.heappush(h, [-(r - a  ) ,a + 1, r])
                #print(" > push", [-(r - a  ) ,a + 1, r])
        #print(res[1:n+1])
        print(" ".join(list(map(str, res[1:n+1]))))








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
        input = """1
200000"""
        output = """1
1 2
2 1 3
3 1 2 4
2 4 1 3 5
3 4 1 5 2 6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()