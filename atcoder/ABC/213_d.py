import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint
    INF = 1 << 63
    def do():
        from heapq import heappop, heappush, heapify
        n = int(input())

        g = [[] for _ in range(n)]
        for i in range(n-1):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            heappush(g[a], b)
            heappush(g[b], a)
        visited = [False] * n
        parent = [-1] * n
        curpos = 0
        res = []
        while True:
            visited[curpos] = True
            res.append(curpos)

            nextNode = None
            while len(g[curpos]) > 0:
                candidate = heappop(g[curpos])
                if visited[candidate] is True: continue
                nextNode = candidate
                break

            if nextNode is not None:
                parent[nextNode] = curpos
                curpos = nextNode
                continue
            # NextNode is None
            if curpos == 0: break
            curpos = parent[curpos]

        print(" ".join(list(map(lambda x: str(x + 1), res))))

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
        input = """4
1 2
4 2
3 1"""
        output = """1 2 4 2 1 3 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2
1 3
1 4
1 5"""
        output = """1 2 1 3 1 4 1 5 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()