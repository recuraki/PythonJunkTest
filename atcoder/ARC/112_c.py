import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    e = [[] for _ in range(n)]
    for i in range(n-1):
        x = dat[i]
        e[x-1].append(i+1)
    print(e)
    depth = [0] * n
    from collections import deque
    q = deque([])
    maxdepth = 0 # 最大の深さ
    depthTable = [[] for _ in range(n)] # その深さのテーブル
    q.append((0, 0))
    while len(q) > 0:
        curNode, curDepth = q.popleft()
        depthTable[curDepth].append(curNode) # 深さテーブルへの追加
        for nextNode in e[curNode]: # 次の探索
            q.append((nextNode, curDepth + 1))
    print(depthTable)
    table = [None] * n # win, lose, turn
    # turn: 偶数ならダメージがない、奇数ならターンが変わる
    for dep in range(n-1, -1, -1): # 葉からたどる
        for curNode in depthTable[dep]: # 同じ改装は適当にたどる
            if len(e[curNode]) == 0: # 葉
                print("I'm child", curNode)
                table[curNode] = (1, 0, 0)
                continue

            # 子がいるときの処理
            oddNodesCnt = 0
            evenNodesCnt = 0
            oddNodesScore = []
            winScore = 0
            loseScore = 0

            for childNode in e[curNode]:
                print(">>", table[childNode], childNode)
                win, lose, turn = table[childNode]
                if turn % 2 == 0: # リスクがない
                    print("no risk", win)
                    winScore += win
                    loseScore += lose
                    evenNodesCnt += 1
                    continue
                # リスクあり
                oddNodesScore.append((win, lose))

            # oddが出たので
            oddNodesScore.sort(reverse=True)
            # ターン変更は全てとるので、どのようにとるか
            myTurn = (evenNodesCnt + 1) % 2

            for i in range(len(oddNodesScore)):
                win, lose = oddNodesScore[i]
                if i % 2 == 0:
                    winScore += win
                    loseScore += lose
                else:
                    winScore += lose
                    loseScore += win

            if myTurn % 2 == 1:
                table[curNode] = ( loseScore, winScore + 1 ,(myTurn ) % 2)
            else:
                table[curNode] = ( winScore + 1, loseScore ,(myTurn ) % 2)


    print(table)
    print(table[0][0] )










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
        input = """10
1 2 3 4 5 6 7 8 9"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
1 2 3 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
1 1 3 1 3 6 7 6 6"""
        output = """5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()