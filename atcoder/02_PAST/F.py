import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import heapq
    h = []
    import collections
    canjobs = []
    for i in range(n+1):
        canjobs.append([])

    curjobs = []
    for _ in range(n):
        a,b = map(int, input().split())
        canjobs[a].append(b)
    #print(canjobs)
    res = 0
    result = []
    heapq.heapify(curjobs)

    for i in range(1, n+1):
        for val in canjobs[i]:
            #print(val)
            heapq.heappush(curjobs, -val)
        high = heapq.heappop(curjobs)
        high = -high
        res += high
        result.append(str(res))
    print("\n".join(result))



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
1 3
2 2
2 4"""
        output = """3
7
9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
5 3
4 1
3 4
2 1
1 5"""
        output = """5
6
10
11
14"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
1 8
1 6
2 9
3 1
3 2
4 1"""
        output = """8
17
23
25
26
27"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()