import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # ABC228B: フロイドの循環検出法アルゴリズム
    # 空間計算量: 初期データを除いてO(1)
    # 時間計算量: O(N)相当。
    n, x = map(int, input().split())
    dat = list(map(lambda a: int(a)-1 , input().split()))
    hare = tortoise = x-1 # 初期位置
    while True:
        hare = dat[dat[hare]] # 2歩進む
        tortoise = dat[tortoise] # 1歩進む
        if hare == tortoise: break
    hare = x - 1 # ウサギだけ戻す
    stepCountStartToLoopStart = 0 # スタートから巡回の開始位置までの距離
    while True:
        stepCountStartToLoopStart += 1
        hare = dat[hare] # 1歩進む
        tortoise = dat[tortoise] # 1歩進む
        if hare == tortoise: break
    nodeNumLoopStart = hare # 循環の開始位置
    cycleLen = 0 # 循環の長さ
    hare = tortoise = nodeNumLoopStart
    while True:
        cycleLen += 1
        tortoise = dat[tortoise]
        hare = dat[dat[hare]]
        if tortoise == hare: break
    ans = 0
    tortoise = x - 1
    # ここまでが典型のフロイドの循環検出法アルゴリズム
    print(nodeNumLoopStart, cycleLen, stepCountStartToLoopStart )

    # シミュレーションの開始: 今回はループの中からスタートする場合もあるので頑張る必要がある
    alreadyStepLoopStart = False # ループノードを一度でも踏んだか？
    isStepStartNode = False # スタートノードを踏んでしまったか？
    if tortoise == nodeNumLoopStart: alreadyStepLoopStart = True
    while True:
        tortoise = dat[tortoise]
        if alreadyStepLoopStart and tortoise == nodeNumLoopStart: break
        if tortoise == nodeNumLoopStart: alreadyStepLoopStart = True
        if tortoise == x-1:
            isStepStartNode = True
            continue
        # 計算中にスタートノードを踏んだ後のステップは全てダブルカウントなので回収する
        if isStepStartNode: ans -= 1
        else: ans += 1
    print(ans + 1)



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
        input = """4 2
3 1 1 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20 12
7 11 10 1 7 20 14 2 17 3 2 5 19 20 8 14 18 2 10 10"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """20 1
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 9"""
        output = """20"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_21")
        input = """2 1
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_32(self):
        print("test_input_21")
        input = """3 1
2 3 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_33(self):
        print("test_input_21")
        input = """3 3
2 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_332(self):
        print("test_input_21")
        input = """5 2
2 3 4 5 2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_331(self):
        print("test_input_21")
        input = """5 1
2 3 4 5 2"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_333(self):
        print("test_input_21")
        input = """5 3
2 3 4 5 2"""
        output = """4"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()