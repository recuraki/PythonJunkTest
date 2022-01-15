import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    # ABC-228C O(N)
    import sys
    input = sys.stdin.readline
    def do():
        n, k = map(int, input().split())
        original = []
        data = [0] * 1201
        for _ in range(n):
            p1, p2, p3 = map(int, input().split())
            original.append( p1+p2+p3 ) # 元データを保存する（結果表示のため)
            data[p1+p2+p3] += 1 # 各点数の分布を記録
        # 累積和を取る
        cum = [0] * 1202
        for i in range(1201): cum[i+1] = cum[i] + data[i] # これで累積和終わり
        f = lambda a, b: cum[b] - cum[a]  # 累積和クエリ query [a, b)
        # 各人が何番目に入れるかを判定
        for x in original:
            canrank = f(x+300+1, 1200 + 1) + 1 # (その人が4日目に300点の時に上位にいる人) + 1
            print("Yes" if canrank <= k else "No")
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
        input = """3 1
178 205 132
112 220 96
36 64 20"""
        output = """Yes
Yes
No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
300 300 300
200 200 200"""
        output = """Yes
Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 2
127 235 78
192 134 298
28 56 42
96 120 250"""
        output = """Yes
Yes
No
Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()