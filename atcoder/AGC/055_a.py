import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import random
    import sys

    n = 4
    s = "A" * n + "B" * n + "C" * n
    l = list(s)
    random.shuffle(l)
    s = "".join(l)
    s = "CCACABBCBABA"
    # s = "AABBCC"
    # s = "ABCCBA"
    s = "ABCABC"

    n = len(s) // 3
    print(s)

    import itertools
    class CumSum1D():
        def __init__(self):
            pass

        def load(self, a):
            self.sdat = list(itertools.accumulate(itertools.chain([0], a)))

        def query(self, l, r):  # query [a, b)
            return self.sdat[r] - self.sdat[l]

    allfin = False

    def do(s: str):
        """
        ind[char][cnt]: charがcnt個出た場所
        """

        print(s)
        l = list(s)
        lenl = len(l)  # kの長さ
        cnt = [[0] * len(l) for _ in range(2 + 1)]
        indchar = [[0] * (n + 1) for _ in range(2 + 1)]
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        print(indchar)
        for i in range(len(l)):
            if l[i] == "A":
                l[i] = 0
                cnt[0][i] += 1
                cnt0 += 1
                indchar[0][cnt0] = i
            elif l[i] == "B":
                l[i] = 1
                cnt[1][i] += 1
                cnt1 += 1
                indchar[1][cnt1] = i
            elif l[i] == "C":
                l[i] = 2
                cnt[2][i] += 1
                cnt2 += 1
                indchar[2][cnt2] = i

        print(l)
        cum = [CumSum1D() for _ in range(3)]
        for i in range(3):
            print("cnt", cnt[i])
            cum[i].load(cnt[i])
        for i in range(3):
            print("indc", indchar[i])

        patorig = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

        def func(curind, target, need):
            # curind: よりもあとで target: の数字がneed: 個いじょうあるか？
            ans = cum[target].query(curind + 1, lenl)
            print("call func", "curind", curind + 1, "tar", target, "ne", need, "ans", ans, ans >= need)
            if ans >= need: return True
            return False

        def main(patnum, fixed, nokori, loop):  # patnum = 今回使うパターン
            if patnum == 6:
                if sum(canpat) == n:
                    print("FIN!", canpat)
                    print(loop)
                    print(patorig)
                    allfin[0] = True
                    return True
                else:
                    print("!!!")
                    return False
            a, b, c = patorig[loop[patnum]]
            print("main", patnum, fixed, nokori, canpat, loop, a, b, c, patorig, loop, patnum)

            # print("Pat", a, b, c, "noko", nokori, "fix", fixed)
            # 何個作れるかを計算する
            """
            まず、１文字目を作るために
            """
            ok = 0
            ng = nokori + 1
            # a, b, cの順に作りたいです
            while (abs(ok - ng) > 1):
                print(" patloop", patnum, ok, ng, "pat=", a, b, c)
                mid = (ok + ng) // 2
                print("try", "mid", mid, "fixed", fixed, "indchar", indchar[a][fixed])
                # midが作りたい数です
                # 決まったものはないので、それを踏まえて必要な数 少なくともこれが通らないと意味がない
                if (func(max(indchar[a][fixed + mid], indchar[b][fixed]), b, mid)) is False:
                    ng = mid
                    continue
                print(" ok", "mid", mid, "a,b", a, b)
                # 引き続き、bの後で作れるかを計算する
                if (func(max(indchar[a][fixed + mid], indchar[b][fixed + mid], indchar[c][fixed]), c, mid)) is False:
                    ng = mid
                    continue
                # これで、後段が通るのか考える
                ok = mid
            # okが作れるので、
            print(a, b, c, "ok", ok)
            fixed += ok
            nokori -= ok
            if allfin[0]: return True
            canpat[patnum] = ok
            return main(patnum + 1, fixed, nokori, loop)

        import itertools
        canpat = [0] * 6
        allfin = [False]
        for loop in itertools.permutations([0, 1, 2, 3, 4, 5]):
            print("!!!!!!", loop)
            if allfin[0]: return True
            nokori = n  # 各文字が残っている数
            fixed = 0  # 決まった数(この数文がoffset)
            for i in range(6): canpat[i] = 0
            main(0, fixed, nokori, loop)
            if allfin[0]: return True
            print(patorig)

    do(s)
    # [ok, ng) for max value
    # (ng, ok] for min value
    # CATION: ok is result  (NOT mid)


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
ABCCBA"""
        output = """111222"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
AABCBCAACBCB"""
        output = """111211241244"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()