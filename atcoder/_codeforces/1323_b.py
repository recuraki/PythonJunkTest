import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    n,m,k = map(int, input().split())
    data = input().split()
    datb = input().split()

    divs = make_divisors(k)
    rects = []
    # 面積kの四角形(x,y)を列挙
    for x in divs:
        rects.append((x, k // x))

    from collections import Counter, defaultdict

    # 配列a,bから連続した1の長さの個数をカウントする辞書を生成
    # [1,1,1,0,1,1,1,0,1,1] -> [3,3,2]の長さなので -> {3:2, 2:1}という辞書になる
    da = defaultdict(int)
    db = defaultdict(int)
    cnt = 0
    l = len(data)
    for i in range(l):
        if data[i] == "1":
            cnt += 1
        if data[i] == "0" or i == l - 1:
            da[cnt] += 1
            cnt = 0

    cnt = 0
    l = len(datb)
    for i in range(l):
        if datb[i] == "1":
            cnt += 1
        if datb[i] == "0" or i == l - 1:
            db[cnt] += 1
            cnt = 0

    # 数える
    res = 0
    for lx in da:
        for ly in db:
            for x, y in rects:
                # aとbから作られるx*yの四角形の数
                reccount = da[lx] * db[ly]
                #print("{0} x {1} count = {4}, find {2} x {3} rect".format(lx, ly, x, y, reccount))
                cx = lx - x
                cy = ly - y
                if cx > -1 and cy > -1:
                    # 作れるなら足す
                    cannum = (cx + 1) * (cy + 1) * reccount
                    res += cannum
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
        input = """3 3 2
1 0 1
1 1 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5 4
1 1 1
1 1 1 1 1"""
        output = """14"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_23")
        input = """1 1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_234")
        input = """1 1 1
0
1"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_2345")
        input = """1 1 1
1
0"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()