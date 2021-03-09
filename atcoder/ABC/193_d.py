import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    k = int(input())
    s = input()
    t = input()
    from copy import deepcopy
    nokori = [k] * 10
    nokori[0] = 0
    cards = [0] * 10
    cardt = [0] * 10

    numTotal = 0  # 全部の手数
    numWon = 0  # 勝った手数
    numLose = 0  # 負けた手数

    def isWin():
        scores = scoret = 0
        for i in range(1, 10):
            scores += i * 10**cards[i]
            scoret += i * 10**cardt[i]
        #print(scores, "vs", scoret)
        if scores > scoret:
            #print("win")
            return True
        return False
    for i in range(4):
        x = int(s[i])
        nokori[x] -= 1
        cards[x] += 1
        x = int(t[i])
        nokori[x] -= 1
        cardt[x] += 1
    onokori = deepcopy(nokori)
    ocards = deepcopy(cards)
    ocardt = deepcopy(cardt)
    for i in range(1, 10): # s がとろうとするもの
        nokori = deepcopy(onokori)
        cards = deepcopy(ocards)
        #cardt = deepcopy(ocardt)
        if nokori[i] <= 0: # s はiをとれない
            continue
        sCount = nokori[i] # sがこれをとりうる可能性
        nokori[i] -= 1 # i をとる
        cards[i] += 1 # iをとった
        for j in range(1, 10):
            cardt = deepcopy(ocardt) #やっていく
            if nokori[j] <= 0:  # j はiをとれない
                continue
            tCount = nokori[j]  # sがこれをとりうる可能性
            nokori[j] -= 1  # i をとる
            cardt[j] += 1
            numTotal += sCount * tCount
            if isWin(): # 勝てるか？
                numWon += sCount * tCount
            else:
                numLose += sCount * tCount
    print(numWon / numTotal)


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
        input = """2
1144#
2233#"""
        output = """0.4444444444444444"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
9988#
1122#"""
        output = """1.0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
1122#
2228#"""
        output = """0.001932367149758454"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """100000
3226#
3597#"""
        output = """0.6296297942426154"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()