import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        nxt = [None] * n
        for i in range(n): nxt[i] = (i + dat[i]) % n # next

        # フロイドの循環検出アルゴリズムここから
        hare = tortoise = 0  # 初期位置
        while True:
            hare = nxt[nxt[hare]]  # 2歩進む
            tortoise = nxt[tortoise]  # 1歩進む
            if hare == tortoise: break
        hare = 0  # ウサギだけスタートに戻す
        stepCountStartToLoopStart = 0  # スタートから巡回の開始位置までの距離
        while True:
            stepCountStartToLoopStart += 1
            hare = nxt[hare]  # 1歩進む
            tortoise = nxt[tortoise]  # 1歩進む
            if hare == tortoise: break
        nodeNumLoopStart = hare  # 循環の開始位置
        cycleLen = 0  # 循環の長さ
        hare = tortoise = nodeNumLoopStart
        while True:
            cycleLen += 1
            tortoise = nxt[tortoise]
            hare = nxt[nxt[hare]]
            if tortoise == hare: break
        # フロイドの循環検出アルゴリズムここまで

        # ここから循環１サイクルでかかるコストを計算する
        cycleCost = dat[nodeNumLoopStart]
        i = nxt[nodeNumLoopStart]
        print(i, nodeNumLoopStart)
        while i != nodeNumLoopStart:
            cycleCost += dat[i]
            i = nxt[i]
        # ここまで循環コスト

        # スタートから循環位置まで移動する
        ans = 0
        i = 0
        while i != nodeNumLoopStart:
            ans += dat[i]
            i = nxt[i]
            k -= 1
            if k == 0: # そもそもその前にkが0になればそれが応え
                print(ans)
                return
        # 今、循環のスタート位置にいるので、まず、何周できたかのコスト計算
        ans += cycleCost * (k // cycleLen)
        k %= cycleLen
        # あとはk回回ればいい
        i = nodeNumLoopStart
        while k > 0:
            ans += dat[i]
            i = nxt[i]
            k -= 1
        print(ans)

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
        input = """5 3
2 1 6 3 1"""
        output = """11"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 1000000000000
260522 914575 436426 979445 648772 690081 933447 190629 703497 47202"""
        output = """826617499998784056"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()