import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from collections import deque
    n, m, k =map(int, input().split())

    directcount = [0] * n # node_iが直接接続しているノードの数
    visited = [-1]  * n # nodeの色,
    colorcount = [-1] * n # 各色が何個のノードを持つか
    # グラフの初期化
    g = []
    for _ in range(n):
        g.append(deque(list()))

    # グラフの生成
    for i in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1 # 1origin -> 0 origin
        g[a].append(b)
        g[b].append(a)
        # 直接接続されているノードの数
        directcount[a] += 1
        directcount[b] += 1

    # dfs 連結したグラフごとにそのグラフの最初に探索したnodeの色に染める
    q = deque(list()) #探索キュー
    for i in range(n):
        q.append(i)
        color = i
        cnt = 1
        while len(q) > 0:
            nextnode = q.popleft() # 次の探索
            if visited[nextnode] != -1:
                continue
            visited[nextnode] = color
            q.extend(g[nextnode]) # nextnodeの辺を足す
            cnt += 1
        # 探索が終わったらその色のノードの数を記録
        colorcount[color]  = cnt - 1

    # res[i] = ノードの色, その色のノードの数 - そのノードが直接接続しているノード数 - 自分自身(1)　で初期化する
    res = [[visited[i], colorcount[visited[i]] - (directcount[i] + 1)] for i in range(n)]

    # ブロックリスト
    for i in range(k):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1 # 1 origin -> 0 origin
        # ブロック関係が同じ色だとするなら
        if res[c][0] == res[d][0]:
            # 友達になれると思っていた数を1つ減らす
            res[c][1] -= 1
            res[d][1] -= 1


    # 結果の表示
    print(" ".join(list(map(lambda x: str(x[1]), res))))



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
        input = """4 4 1
2 1
1 3
3 2
3 4
4 1"""
        output = """0 1 0 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 10 0
1 2
1 3
1 4
1 5
3 2
2 4
2 5
4 3
5 3
4 5"""
        output = """0 0 0 0 0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1"""
        output = """1 3 5 4 3 3 3 3 1 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()