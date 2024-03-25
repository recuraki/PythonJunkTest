import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from itertools import combinations
    n, w = map(int, input().split())
    dat = list(map(int, input().split()))
    ans = set() # 結果の種類数
    for cnt in (1,2,3): # 1,2,3個選んだ時
        for selected in combinations(dat, cnt): # datの値をcnt個選ぶ全ての組み合わせ
            # ここで、selectedには(3,6,10)や(1,2)や(4)のようにcnt個の重さの値が入っている
            if sum(selected) <= w: # なので、その和がw以下なら
                ans.add(sum(selected)) # その和を重さの種類としてsetに淹れる
    print(len(ans)) # で、種類数をひょぅじしてやれば良い



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
        input = """2 10
1 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1
2 3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 12
3 3 3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7 251
202 20 5 1 4 2 100"""
        output = """48"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()