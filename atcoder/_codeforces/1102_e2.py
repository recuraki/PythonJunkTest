import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 998244353

    n = int(input())
    dat = list(map(int, input().split()))
    num_firstpos = dict()
    num_lastpos = dict()

    # ある数字が
    # num_firstpos: 最初に出現する場所
    # num_lastpos: 最後に出現する場所
    for i in range(n):
        num_lastpos[dat[i]] = i
        if dat[i] not in num_firstpos:
            num_firstpos[dat[i]] = i

    # 結果の初期値は1通り
    res = 1

    # dat[0]の読み込み
    cur = 0
    skipto = num_lastpos[dat[0]]

    # print(num_firstpos)
    # print(num_lastpos)

    # 最後の文字まで読み込む
    while cur < (n - 1):
        # インクリメントと文字の読み込み
        cur += 1
        curval = dat[cur]

        # print("proc: curval: {0} cur: {1} skipto:{2}".format(curval, cur, skipto))

        # もし、ロックされていないて、
        if skipto <= cur:
            # この数字が過去に出ていない時に限って
            # (過去に出ているなら値はロックされているので)
            if num_firstpos[curval] == cur:
                # この数字の取りうるのは2通りなので、結果を倍にする
                res *= 2
                res %= mod

        skipto = max(skipto, num_lastpos[curval])

    # 結果の表示
    print(res)


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
        input = """10
6 7 7 7 7 7 3 3 7 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """9
1 2 3 2 2 2 1 6 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_111(self):
        print("test_input_111")
        input = """100
94 69 43 36 54 93 30 74 56 95 70 49 11 36 57 30 59 3 52 59 90 82 39 67 32 8 80 64 8 65 51 48 89 90 35 4 54 66 96 68 90 30 4 13 97 41 90 85 17 45 94 31 58 4 39 76 95 92 59 67 46 96 55 82 64 20 20 83 46 37 15 60 37 79 45 47 63 73 76 31 52 36 32 49 26 61 91 31 25 62 90 65 65 5 94 7 15 97 88 68"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_1111(self):
        print("test_input_1111")
        input = """100
23 39 85 46 97 72 41 70 37 18 8 40 33 61 12 79 51 78 61 66 85 97 78 14 70 47 100 40 15 40 61 52 19 30 14 91 82 56 10 6 68 24 97 61 31 78 18 45 88 6 37 38 51 86 37 42 58 30 79 56 50 14 61 18 13 20 57 3 93 15 24 74 32 21 71 93 2 66 25 75 75 10 86 82 30 31 6 49 15 33 100 35 1 96 87 83 29 21 41 22"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()