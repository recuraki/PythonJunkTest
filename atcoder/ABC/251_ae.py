import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n = int(input())
    indat = list(map(int, input().split()))
    def func(dat):
        # この関数は「巡回がないとして」動物1 (dat[0])に餌をやったときの動物Nまで餌をやるのに最小のコストを計算する
        ans = [1<<61] * n
        ans[0] = dat[0] # 動物1に餌をやった
        ans[1] = dat[0] # 動物1に餌をやった(ので、動物2まで届く)
        for i in range(2, n): # その先をシミュレート
            ans[i] = min(ans[i], ans[i - 2] + dat[i - 1])  # Pat1
            ans[i] = min(ans[i], ans[i - 1] + dat[i - 1])  # Pat2
            ans[i] = min(ans[i], ans[i - 1] + dat[i])      # Pat3
        return ans[n-1] # 最後まで餌をやるのにかかるコスト
    ans1 = func(indat) # 初期状態のコスト
    import collections
    indat = collections.deque(indat)
    indat.rotate(1) # 初期状態を一個ローテート [1,2,3] -> [2,3,1]にする
    ans2 = func(list(indat)) # またDP計算。これは実質、動物Nに餌を挙げることで動物1に餌をあげたパターン
    print(min(ans1, ans2)) # その最小が応え


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
2 5 3 2 5"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """20
29 27 79 27 30 4 93 89 44 88 70 75 96 3 78 39 97 12 53 62"""
        output = """426"""
        self.assertIO(input, output)

    def test_input_21(self):
        print("test_input_21")
        input = """2
10 20"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()