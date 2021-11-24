import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63

    """
    bi-dir
    単純グラフ
    アイデア: 橋を探して分解する
    アイデア: その中が矛盾がないなら、辺の付け方は、ノード数をnとして
    
    """
    def do():
        m = 998244353
        n, m = map(int, input().split())
        visited = [False] * n
        g = [list() for _ in range(n)]
        for _ in range(m):
            x, y = map(int, input().split())
            x -= 1
            y -= 1
            g[x].append(y)
            g[y].append(x)

        groups = 0
        parents = [-1] * n
        from collections import deque
        for start in range(n):
            hasloop = False
            if visited[start]: continue # 既に探索済み
            groups += 1
            visited[start] = True # 親を探索済みにする
            q = deque([start])
            nodes = 0
            edges = 0
            while len(q) > 0:
                curNode = q.popleft()
                nodes += 1
                edges += len(g[curNode])
                for nextNode in g[curNode]:
                    # これは無視
                    if nextNode == parents[curNode]: continue
                    # もし、既知のノードならループを蟻にする
                    if visited[nextNode]:
                        hasloop = True
                        continue
                    visited[nextNode] = True
                    parents[nextNode] = curNode
                    q.append(nextNode)
            edges //= 2

            if hasloop is False:
                print(0)
                return
            sa = edges - nodes
            if sa > 3 :
                print(0)
                return
        print(pow(2, groups, m))

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
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
1 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7 7
1 2
2 3
3 4
4 2
5 6
6 7
7 5"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """4 3
1 2
2 3
3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_312(self):
        print("test_input_312")
        input = """9 9
1 2
2 3
3 1
4 5
5 6
6 4
7 8
8 9
9 7"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3132(self):
        print("test_input_3132")
        input = """9 8
1 2
2 3
3 1
4 5
5 6
6 4
7 8
8 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_31321(self):
        print("test_input_31321")
        input = """5 4
1 2
2 3
3 1
4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_313211(self):
        print("test_input_313211")
        input = """4 6
1 2
2 4
3 4
1 3
1 4
2 3
"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3132111(self):
        print("test_input_3132111")
        input = """4 5
1 2
2 4
3 4
1 3
1 4
"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3132111(self):
        print("test_input_3132111")
        input = """4 5
1 2
2 4
3 4
1 3
1 4
"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()