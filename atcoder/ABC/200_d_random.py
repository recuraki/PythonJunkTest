import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from random import randint
    def do():
        n = int(input())
        dat = list(map(lambda x: int(x)%200, input().split()))
        resa = None
        for trycount in range(200000): # 200000回くらい乱択する
            # 0 = だれも取らない, 1 = Bがとる, 2 = Cがとる
            bit = [randint(0,2) for _ in range(n)] # [1,0,1,0]とか作る
            setB = set() # 取った値のindex リスト
            setC = set() # 取った値のindex リスト
            amariB = 0 # 取った値を足して % 200するやつ
            amariC = 0 # 取った値を足して % 200するやつ
            if bit.count(1)==0: continue
            if bit.count(2)==0: continue
            for i in range(n): # 各ビットを処理
                if bit[i] == 1: # 立っていたら
                    setB.add(i+1) # 選択したset(unorderedmap)に入れて
                    amariB += dat[i] # 合計を足す
                elif bit[i] == 2: # 立っていたら
                    setC.add(i+1) # 選択したset(unorderedmap)に入れて
                    amariC += dat[i] # 合計を足す
            amariB %= 200
            amariC %= 200
            if amariB == amariC:
                resa = list(setB)
                resb = list(setC)
                break
        if resa is None:
            print("No")
            return
        outputa = []
        outputb = []
        outputa.append(len(resa))
        outputa.extend(resa)
        outputb.append(len(resb))
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

if __name__ == "__main__":
    unittest.main()