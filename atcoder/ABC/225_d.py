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
    基本的な考え方。
    最初はroot(-1)を基にするツリーを持っているとする。
    また、終点はend(-1)としよう
    parent(前のノード)
    chile(後ろのノード
    """
    def do():
        from collections import deque
        n, qnum = map(int, input().split())
        parent = [-1] * (n + 1)
        child = [-1] * (n + 1)
        for q in range(qnum):
            query = input().split()
            qpat = int(query[0])
            if qpat == 1: # xの後ろにyを結合
                x, y = int(query[1]), int(query[2])
                child[x] = y
                parent[y] = x
            elif qpat == 2: # xのうしろと、yのまえを結合する
                x, y = int(query[1]), int(query[2])
                child[x] = -1
                parent[y] = -1

            elif qpat == 3: #表示する
                x = int(query[1])
                #print("query", x)
                #print(parent)
                #print(child)

                ans = deque([x])
                # 前にたどっていく(left)
                cur = x
                while True:
                    #print("cur", cur, "parent", parent[cur])
                    cur = parent[cur]

                    if cur == -1: break
                    ans.appendleft(cur)

                cur = x
                while True:
                    #print("cur", cur, "child", child[cur])
                    cur = child[cur]
                    if cur == -1: break
                    ans.append(cur)
                ans.appendleft(len(ans))
                print(" ".join(list(map(str, ans))))
            else:
                assert False
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
        input = """7 14
1 6 3
1 4 1
1 5 2
1 2 7
1 3 5
3 2
3 4
3 6
2 3 5
2 4 1
1 1 5
3 2
3 4
3 6"""
        output = """5 6 3 5 2 7
2 4 1
5 6 3 5 2 7
4 1 5 2 7
1 4
2 6 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()