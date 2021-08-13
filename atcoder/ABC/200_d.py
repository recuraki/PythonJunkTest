import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    from copy import deepcopy
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        buf = []
        for x in dat:
            buf.append(x%200)
        dp = [None] * 200
        dp[0] = set() # 0は初期状態
        resb = None
        for bufi in range(len(buf)): # １つずつ、取ったとき、取らない時を処理
            newdp = [None] * 200 # 更新用のDPテーブル
            x = buf[bufi]
            for i in range(200): # 各DP更新
                if dp[i] == None: # その組がないならDP更新できない
                    continue
                nextind = (i + x) % 200 # 次のDP index
                nextset = deepcopy(dp[i]) # 次のDPテーブルに書くset
                nextset.add(bufi+1) # さっきのsetに自分を追加
                if dp[nextind] is not None and len(dp[nextind]) != 0:
                    # もし、既にそのあまりにできて、
                    # かつ、それがlen==0 というのは、初期値で入れたdp[0]でなければ
                    # それを結果としてループを抜ける
                    resa = list(dp[nextind])
                    resb = list(nextset)
                    break
                # そうでない場合、次に進むため、次のテーブルを更新
                newdp[nextind] = nextset
            # dpテーブルをnewdpに移す。使われなかった値を移す。
            for i in range(200):
                if newdp[i] == None:
                    newdp[i] = dp[i]
            dp = newdp
            if resb is not None:
                break
        # ループを抜けても、結果が入っていないときのみNG
        if resb is None:
            print("No")
            return

        outputa = []
        outputb = []
        outputa .append(len(resa))
        outputa.extend(resa)
        outputb .append(len(resb))
        outputb.extend(resb)
        print("Yes")
        print(" ".join(list(map(str, outputa))))
        print(" ".join(list(map(str, outputb))))

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
        input = """5
180 186 189 191 218"""
        output = """Yes
1 1
2 3 4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
123 523"""
        output = """Yes
1 1
1 2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
2013 1012 2765 2021 508 6971"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_34")
        input = """2
1 2"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_41(self):
        print("test_input_41")
        input = """4
1 2 196 4"""
        output = """No"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()