import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
"""
各色をdefaultdictでintとる。

STEP1: 前処理。
rでlのnum != 0 があれば消しこむ。costは0

STEP1-2:
さて、oddな数しかない色は、LRのodd同士で消しこんでしまいたい。
oddなモノだけカウントしておく。そして、oddな者同士をcost 1で消す
もし、oddな色が余ってしまった場合、適当な色に変えてcost1で消す

STEP2: 形を変えるだけで消せるものを探す
- L, R両方を色=keyで見ていく。%2まで消せる。costはそれぞれ1

STEP3: 色を変えるだけで消せるものを探す。
ここで、l,rを比較して、minの方をcost 1する。これは多い方は色を消せば消しこめるから。色を区別しなくていい。

STEP4: 色も形も変える
これで残ったものはある片側のソックスのみであり、絶対に偶数である。なので、//2した数を*2すればいい。
つまり、あるソックスの色を変えて、形も変える costは1

"""
def resolve():

    import sys
    #input = sys.stdin.readline
    from pprint import pprint
    from collections import defaultdict
    def do():
        res = 0
        n, lcnt, rcnt = map(int, input().split())
        dat = list(map(int, input().split()))
        ldat = dat[:lcnt]
        rdat = dat[lcnt:]
        #print(ldat)
        #print(rdat)
        lsocks = defaultdict(int)
        rsocks = defaultdict(int)
        for x in ldat:
            lsocks[x] += 1
        for x in rdat:
            if lsocks[x] > 0: # if r have pair
                lsocks[x] -= 1 # remove
                # can pair so cnt --
                lcnt -= 1
                rcnt -= 1
                if lsocks[x] == 0: # if not need erase
                    del lsocks[x]
                continue
            else: # if don't have pair
                rsocks[x] += 1 # inc
        # STEP1 end
        #print("step1,end", res)

        # STEP1-2 odd count
        loddlist = []
        roddlist = []
        for k in lsocks.keys():
            if lsocks[k] % 2 == 1:
                loddlist.append(k)
        for k in rsocks.keys():
            if rsocks[k] % 2 == 1:
                roddlist.append(k)
        minoddnum = min(len(roddlist), len(loddlist))
        for i in range(minoddnum):
            loddind, roddind = loddlist[i], roddlist[i]
            lsocks[loddind] -= 1
            rsocks[roddind] -= 1
            lcnt -= 1
            rcnt -= 1
            res += 1

        overoddcnt = max(len(roddlist), len(loddlist)) - min(len(roddlist), len(loddlist))

        if len(roddlist) == len(loddlist):
            pass
        elif len(roddlist) > len(loddlist): # r have more odd
            for k in roddlist[minoddnum:]:
                rsocks[k] -= 1
                rcnt -= 1
                res += 1
            for k in lsocks.keys():
                if overoddcnt <= 0:
                    break
                canerase = min(lsocks[k], overoddcnt)
                lsocks[k] -= canerase
                lcnt -= canerase
                overoddcnt -= canerase
        elif len(roddlist) < len(loddlist): # r have more odd
            for k in loddlist[minoddnum:]:
                lsocks[k] -= 1
                lcnt -= 1
                res += 1
            for k in rsocks.keys():
                if overoddcnt <= 0:
                    break
                canerase = min(rsocks[k], overoddcnt)
                rsocks[k] -= canerase
                rcnt -= canerase
                overoddcnt -= canerase

        #print(lsocks, lcnt)
        #print(rsocks, rcnt)
        #print("step1-2 end", res)

        # STEP2: change color
        for k in lsocks.keys():
            val = lsocks[k]
            if val > 1: # can create pair
                canmakepair = val // 2
                res += canmakepair
                lsocks[k] -= (canmakepair * 2)
                lcnt -= (canmakepair * 2)
        for k in rsocks.keys():
            val = rsocks[k]
            if val > 1: # can create pair
                canmakepair = val // 2
                res += canmakepair
                rsocks[k] -= (canmakepair * 2)
                rcnt -= (canmakepair * 2)
        # STEP2 end
        #print("step2,end", res)
        # STEP3
        # l < r then can l erase
        lcnt, rcnt = min(lcnt, rcnt), max(lcnt, rcnt)
        res += lcnt
        rcnt -= lcnt
        # STEP3 end
        #print("step3,end", res)
        # STEP4
        res += rcnt
        # STEP4 end
        print(res)

    q = int(input())
    for _ in range(q):
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
        input = """4
6 3 3
1 2 3 2 2 2
6 2 4
1 1 2 2 2 2
6 5 1
6 5 4 3 2 1
4 0 4
4 4 4 3"""
        output = """2
3
5
3"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_11")
        input = """1
6 6 0
1 2 3 1 2 3
"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()