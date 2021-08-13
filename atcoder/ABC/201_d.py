import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    hhh, www = map(int, input().split())
    maze = []
    score = []


    maze.append(["#"] * (www + 2))
    l = [[None] for _ in range(www + 2)]
    score.append(l)
    for _ in range(hhh):
        l = list("#" + input() + "#")
        maze.append(l)
        l = [[-10000,-10000] for _ in range(www+2)]
        score.append(l)
    maze.append(["#"] * (www + 2))
    l = [[-10000, -10000] for _ in range(www + 2)]
    score.append(l)
    from pprint import pprint
    from copy import deepcopy
    score[1][1] = [0, 0]

    for h in range(hhh+2):
        for w in range(www+2):
            if maze[h][w] == "#":
                continue
            print("---------current", h, w, maze[h][w], score[h][w])
            if (h % 2) == 1:
                if (w % 2) == 1:
                    curturn = 1
                else:
                    curturn = 0
            else:
                if (w % 2) == 0:
                    curturn = 1
                else:
                    curturn = 0


            # go down : 下は気にしなくていい
            nw = w
            nh = h + 1
            score[nh][nw][0] = score[h][w][0]
            score[nh][nw][1] = score[h][w][1]
            print("down next", nh, nw)
            if maze[nh][nw] == "+":
                score[nh][nw][curturn] += 1
            elif maze[nh][nw] == "-":
                score[nh][nw][curturn] -= 1
            print("newset set:", score[nh][nw])

            # go right
            nw = w + 1
            nh = h
            print("right next", nh, nw)
            if score[nh][nw][0] == -10000: # まだ未設定の場合
                # なにも考えずに値をセット
                score[nh][nw][0] = score[h][w][0]
                score[nh][nw][1] = score[h][w][1]
                if maze[nh][nw] == "+":
                    score[nh][nw][curturn] += 1
                elif maze[nh][nw] == "-":
                    score[nh][nw][curturn] -= 1
                print("newset set:", score[nh][nw])

            else: # 違う場合、判断が必要
                nextdiff = score[nh][nw][0] - score[nh][nw][1] # 前のtakahashi優位ポイント
                curdiff = score[h][w][0] - score[h][w][1] # 今のマスの 優位ポイント
                if maze[nh][nw] == "+":
                    if curturn == 0:
                        curdiff += 1
                    else:
                        curdiff -= 1
                elif maze[nh][nw] == "-":
                    if curturn == 0:
                        curdiff -= 1
                    else:
                        curdiff += 1

                if True or curturn == 0: #高橋君始点なら、
                    if nextdiff < curdiff: # もし新しい方が強いなら置き換える
                        score[nh][nw][0] = score[h][w][0]
                        score[nh][nw][1] = score[h][w][1]
                        if maze[nh][nw] == "+":
                            score[nh][nw][0] += 1
                        elif maze[nh][nw] == "-":
                            score[nh][nw][0] -= 1
                #else: # 青木君なら
                #    if nextdiff < curdiff: # もし新しい方が強いなら置き換える
                #        score[nh][nw][0] = score[h][w][0]
                #        score[nh][nw][1] = score[h][w][1]
                #        if maze[nh][nw] == "+":
                #            score[nh][nw][1] += 1
                #        elif maze[nh][nw] == "-":
                #            score[nh][nw][1] -= 1

    pprint(maze)
    print("---")
    pprint(score)
    res = score[hhh][www]
    if res[0] == res[1]:
        print("Draw")
    elif res[0] > res[1]:
        print("Takahashi")
    else:
        print("Aoki")



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
---
+-+
+--"""
        output = """Takahashi"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 4
+++-
-+-+"""
        output = """Aoki"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1
-"""
        output = """Draw"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()