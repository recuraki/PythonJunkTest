import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from collections import deque
    def do():
        a2i = lambda x: ord(x) - ord("a")
        n, m = map(int, input().split())
        s = input()
        target = input()
        posAlphas = [deque([]) for _ in range(26)]
        # まず、最短を求める
        loc = [None] * m
        cur = 0
        for i in range(n):
            val = a2i(s[i])
            posAlphas[val].append(i)
        for i in range(m):
            while s[cur] != target[i]:
                cur += 1
            loc[i] = cur
            cur += 1
        #print(loc)
        #print(posAlphas)
        res = -1
        for i in range(m-1):
            res = max(res, loc[i+1] - loc[i])


        curMax = 10 ** 9 # ひとつ大きい文字の位置(これを以上ではいけない)

        for i in range(m-1, 0, -1): # 上からたどる
            #print("loop", i, loc)
            #print(" > ", posAlphas)
            # なるべく右に
            curLoc = loc[i] # 今の位置
            curChar = a2i(target[i]) # 今の文字
            #print("curLoc, curChar", curLoc, curChar, target[i])
            isRewrite = False # 更新したか？
            while len(posAlphas[curChar]) > 0: #候補があるなら
                canPos = posAlphas[curChar].pop() # 一番大きいのを取る
                #print("canpos", canPos)
                if curMax <= canPos:
                    #print("carmax")
                    continue
                if canPos <= curLoc: # その文字と一緒なら
                    #print("<=")
                    break # 置き換えられないので抜ける
                isRewrite = True
                loc[i] = canPos
                break
            curMax = loc[i]
            res = max(res, loc[i] - loc[i - 1])

        #print("res")
        print(res)


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
abbbc
abc"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """5 2
aaaaa
aa"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """5 5
abcdf
abcdf"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """2 2
ab
ab"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_41(self):
        print("test_input_41")
        input = """9 3
abcabcabc
abc"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_42(self):
        print("test_input_42")
        input = """10 4
abcdabcabc
abcd"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_421(self):
        print("test_input_421")
        input = """11 5
abcabcabcda
abcda"""
        output = """7"""
        self.assertIO(input, output)

    def test_input_422(self):
        print("test_input_422")
        input = """11 3
abcabcabcda
aba"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()