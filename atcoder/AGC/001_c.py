import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    e = []
    for _ in range(n):
        e.append([])
    # 両方への有向辺とする
    for _ in range(n - 1):
        # node = 0 origin
        s, t = map(int, input().split())
        s -= 1
        t -= 1
        e[s].append([t, 1])
        e[t].append([s, 1])
    maxval = max(res)
    erased = [False] * n
    candidate = []
    finalres = 0
    import collections
    for i in range(n):
        if erased[]
        q = collections.deque([])
        q.appendleft([i, 0])
        visited = [False] * n
        while len(q) > 0:
            curNode, curCost = q.popleft()
            visited[curNode] = True
            if curCost > k:
                finalres += 1
                erased[curNode] = True
            for nextNode, nextCost in e[curNode]:
                if visited[nextNode] or erased[nextNode]:
                    continue
                q.append([nextNode, curCost + 1])
        print(i, rescost)
        finalres = min(finalres, rescost)
    print(finalres)



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
        input = """6 2
1 2
3 2
4 2
1 6
5 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5
1 2
3 2
4 2
1 6
5 6"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()