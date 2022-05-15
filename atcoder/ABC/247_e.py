import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from bisect import bisect_left
    n, x, y = map(int, input().split())
    dat = list(map(int, input().split()))
    buf = []
    q = []
    # 入力の配列を、min未満, max超過の数字でsplitする
    for val in dat:
        if y <= val <= x:
            q.append(val)
            continue
        if len(q) > 0: buf.append(q)
        q = []
    if len(q) > 0: buf.append(q)
    # 各分割について数を計算する
    ans = 0
    for dat in buf:
        milist = []  # minのindex list
        malist = []  # maxのindex list
        for i in range(len(dat)): # を作る
            if dat[i] == y: milist.append(i)
            if dat[i] == x: malist.append(i)
        for l in range(len(dat)):  # lを固定して満たせるrを探索
            r = bisect_left(malist, l) # index=l以上のxのindex見つける
            if len(malist) <= r: continue # xが見つからない時は無理
            a = malist[r]
            r = bisect_left(milist, l) # index=l以上のyのindex見つける
            if len(milist) <= r: continue # yが見つからないときは無理
            b = milist[r]
            r = max(a, b) # xかyの見つかったindexの大きい方
            ans += len(dat) - r #それ以上は全部良いRなので組み合わせの数としてadd
    print(ans)


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
        input = """4 3 1
1 2 3 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2 1
1 3 2 4 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 1 1
1 1 1 1 1"""
        output = """15"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 8 1
2 7 1 8 2 8 1 8 2 8"""
        output = """36"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()