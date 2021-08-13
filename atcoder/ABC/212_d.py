import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from heapq import heappop, heappush, heapify
    from collections import defaultdict

    class exhanceHeapq():
        containDict = defaultdict(int)
        willdeleteDict = defaultdict(int)

        def __init__(self, initlist=list()):
            self.q = initlist
            heapify(initlist)

        def pop(self):
            while len(self.q) > 0:
                candidate = heappop(self.q)
                assert self.willdeleteDict[candidate] >= 0
                self.containDict[candidate] -= 1
                if self.willdeleteDict[candidate] > 0:
                    self.willdeleteDict[candidate] -= 1
                else:
                    return candidate

        def push(self, x):
            heappush(self.q, x)
            self.containDict[x] += 1

        def erase(self, x):
            assert self.containDict
            self.willdeleteDict[x] += 1

    INF = 1 << 63

    def do():
        qnum = int(input())
        offset = 0
        pq = exhanceHeapq()
        for _ in range(qnum):
            inp = input().split()
            pat = int(inp[0])
            if pat == 1:
                param = int(inp[1])
                pq.push(param - offset)
                pass
            if pat == 2:
                param = int(inp[1])
                offset += param
                pass
            if pat == 3:
                x = pq.pop()
                print(x + offset)
                pass
    do()


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
        input = """5
1 3
1 5
3
2 2
3"""
        output = """3
7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
1 1000000000
2 1000000000
2 1000000000
2 1000000000
2 1000000000
3"""
        output = """5000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()