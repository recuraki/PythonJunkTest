import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    mod = 998244353

    used = dict()
    n = int(input())
    dat = list(map(int, input().split()))
    used[dat[0]] = True
    res = 1
    lock = False

    count = collections.Counter(dat)

    cur = -1
    count[dat[0]] -= 1
    if count[dat[0]] != 0:
        cur = dat[0]
        lock = True

    print(count)
    for i in range(1, n):
        print("proc:{0} known:{1} remain:{2}".format(dat[i], dat[i] in used, count[dat[i]]))
        count[dat[i]] -= 1

        # もし、ロック中の文字なら、
        if dat[i] == cur and lock is True:
            # そのロックが最後なら
            if count[dat[i]] == 0:
                # もしロックは解除する
                lock = False
                cur = -1
        else:
            # その数字がこれまで出たことのない数字で
            if dat[i] not in used:
                # ロックされていないなら
                if lock is False:
                    # 結果を倍にして
                    print("double")
                    res *= 2
                    res %= mod
                    # 今の数字とする
                    # もしも最後までに再度出現する文字ならロックを実施
                    if count[dat[i]] != 0:
                        cur = dat[i]
                        lock = True
            # 出たことのある数字で、
            else:
                # もしも最後までに再度出現する文字ならロックを実施
                if lock is False:
                    if count[dat[i]] != 0:
                        cur = dat[i]
                        lock = True
        # 既知にする
        used[dat[i]] = True

        print("{0} curlock: {1} res {2} lock {3} count {4}".format(dat[i], cur, res, lock,count[dat[i]]))

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
        output = """2"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_11")
        input = """2
100 1"""
        output = """2"""
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