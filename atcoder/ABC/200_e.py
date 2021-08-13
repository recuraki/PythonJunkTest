import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools
    def do():
        # 累積和lib
        squery = lambda a, b: sdat[b] - sdat[a]  # query [a, b)
        def createSDAT(l):
            return list(itertools.accumulate(itertools.chain([0], l)))
        n, k = map(int, input().split())
        # 0,0, 0,0,0,0 ,1,2,3,4,3,2,1, 0,0,0,0 0,0 をつくる
        l = ([0] * (2 + n)) + list(range(1, n+1)) + list(range(n-1, 0, -1)) + ([0] * (2 + n + 10))
        sdat = createSDAT(l) # 累積和の準備
        for i in range(n*3 + 1): # 上で作ったものをi個 - i + n個目の要素ずつ引く。何個目まで引けるかをチェック
            if k <= squery(i, i+n):
                break
            k -= squery(i, i+n)
        ll = l[i:i+n] # [0,0,1,2]
        ll.reverse() # 結果のリストをひっくりかえす例えば　[0,0,1,2]を切り取ったとき、[2,1,0,0]
        wantmake = i # これが何個目のスライスかを保存。これは結果的に3つの数字を足して、wantmakeにしたいということ。
        for i in range(n): # [2,1,0,0]というのはこの段数で1からスタートが2個, 2からスタートが1個ということであるので
            # k = 個乗った値、でさらにこの何段目まで行けるかを数えていく
            if (k - ll[i]) <= 0:
                break
            k -= ll [i]
        x = i + 1 # で、i段目まで作れるなら、iは0-indexedなので、+1して
        wantmake -= x # x は使ったので、残りは-xしてよくって
        cnt = 0
        for y in range(1, n+1):
            # たかだが、1e6までなので、愚直にループして、k番目まで数えればいい
            z = wantmake - y
            if 1 <= z <= n:
                cnt += 1
            if cnt == k:
                break
        print(x, y, z)
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
        input = """2 5"""
        output = """1 2 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1000000 1000000000000000000"""
        output = """1000000 1000000 1000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9 47"""
        output = """3 1 4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()