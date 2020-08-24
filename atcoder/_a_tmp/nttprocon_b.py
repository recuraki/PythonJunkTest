import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    chrnum = ["2", "3", "4", "5", "6", "7", "8", "9"]
    chrdir = ["R", "L"]
    chrmove = ["F", "B"]

    def do(s):
        chrnum = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # 上に向いていると仮定
        turn = 0
        cnt = 1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y = 0, 0
        #print("call do")
        skipto = -1

        for i in range(len(s)):
            if s[i] == "]":
                modeskip = False
                continue
            if i < skipto:
                continue
            #print("cur >", s[i], x, y, turn)
            if s[i] in chrnum:
                cnt = int(s[i])
            elif s[i] == "R":
                turn += 1 * cnt
                turn %= 4
                cnt = 1
            elif s[i] == "L":
                turn -= 1 * cnt
                turn %= 4
                cnt = 1
            elif s[i] == "F":
                x += dx[turn] * cnt
                y += dy[turn] * cnt
                cnt = 1
            elif s[i] == "B":
                x -= dx[turn] * cnt
                y -= dy[turn] * cnt
                cnt = 1
            elif s[i] == "[":
                news = ""
                modeskip = True
                braket = 1
                while braket > 0:  # "]"まで飛ぶ
                    i += 1
                    if s[i] == "]":
                        braket -= 1
                    if s[i] == "[":
                        braket += 1
                    news += s[i]
                skipto = i
                nx, ny, nturn = do(news)
                #print("  do[", news, "] cnt", cnt, "return ", nx, ny, nturn)
                for i in range(cnt):
                    if turn == 0:
                        x += nx
                        y += ny
                    elif turn == 1:
                        x += ny
                        y -= nx
                    elif turn == 2:
                        x -= nx
                        y -= ny
                    elif turn == 3:
                        x -= ny
                        y += nx
                    turn += nturn
                    turn %= 4
                cnt = 1
        return x, y, turn
    import collections
    n = int(input())
    s = input()
    #print(s)
    stack = collections.deque([])
    x, y, turn = 0, 0, 0
    # turn: 0up, 1right, 2 down 3left

    x,y,turn = do(s)
    print(x, y)


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
FFRFLFRF
"""
        output = """2 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
5B2RL4FL9B
"""
        output = """4 -14"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
4[3B6F5R]"""
        output = """0 0"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """28
3[2[2FR]F4[6B7F]5[RL9[BF]R]]"""
        output = """3 2"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_4")
        input = """4
[FF]"""
        output = """0 2"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()