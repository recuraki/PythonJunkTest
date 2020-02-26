import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    primINF = 2000000000
    matrix = []
    numV = n
    for i in range(n):
        matrix.append(list(map(int, input().split())))

    visited = [False] * numV
    cost = [primINF] * numV # cost
    parent = [-1] * numV # parent node

    cost[0] = 0
    parent[0] = -1

    while True:
        # 訪問済み隣接の最小コストのノードを探索する
        mincost = primINF
        for i in range(n):
            if visited[i] is False and cost[i] < mincost:
                mincost = cost[i]
                u = i
        # 見つからなければ終了する
        if mincost == primINF:
            break
        # 訪問済みにする
        visited[u] = True
        for v in range(n):
            if visited[v] is False and matrix[u][v] != -1:
                if matrix[u][v] < cost[v]:
                    cost[v] = matrix[u][v]
                    parent[v] = u
    res = 0
    for i in range(n):
        if parent[i] != -1:
            res += matrix[i][parent[i]]

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
        input = """5
 -1 2 3 1 -1
 2 -1 -1 4 -1
 3 -1 -1 1 1
 1 4 1 -1 3
 -1 -1 1 3 -1"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()