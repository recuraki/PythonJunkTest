import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from bisect import bisect_right
    n = int(input())
    dat = list(map(int, input().split()))
    total = sum(dat) # 全部の和
    # 作れる整数を列挙する
    cansum = [True] + [False] * (10**5 + 20)
    cannum = []
    for x in dat:
        for i in range(10**5+3, -1, -1):
            if cansum[i] is True: cansum[i+x] = True
    # [T,F,T,T,T] -> [0,2,3,4]に変換 (sorted)
    for i in range(10**5+3):
        if cansum[i]: cannum.append(i)
    # 作れる数を二分探索する。
    l, h = 0, 10**18
    while l <= h:
        mid = (l + h) // 2
        # mid 以下の最大の作れる数をoneofnumとする
        oneofnum = cannum[bisect_right(cannum, mid) - 1]
        # oneofnumあるいは、残った数(totalから引く)のmaxがmid以下なら作れる
        if max(oneofnum, total - oneofnum) <= mid:
            h = mid - 1 # ので、もっと小さい数にトライ
        else:
            l = mid + 1 # 作れない場合はもっと大きい数をトライ
    print(l)

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
8 3 7 2 5"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1000 1"""
        output = """1000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9
3 14 15 9 26 5 35 89 79"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()