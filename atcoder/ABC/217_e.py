import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    def do():
        from heapq import heappop, heappush, heapify
        from collections import deque
        """
        基本的に、queueにほおりこむ。
        """
        n = int(input())
        reserve = deque([])
        pq = []
        heapify(pq)
        for _ in range(n):
            que = input().split()
            if que[0] == "1":
                x = int(que[1])
                reserve.append(x)
                continue
            elif que[0] == "2":
                if len(pq) > 0:
                    res = heappop(pq)
                else:
                    res = reserve.popleft()
                print(res)
                continue
            elif que[0] == "3":
                while len(reserve) > 0:
                    x = reserve.popleft()
                    heappush(pq, x)
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
        input = """8
1 4
1 3
1 2
1 1
3
2
1 0
2"""
        output = """1
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """9
1 5
1 5
1 3
2
3
2
1 6
3
2"""
        output = """5
3
5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()