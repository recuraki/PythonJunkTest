import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class sparseTable(object):
        func = min

        def __init__(self):
            self.table = []
            self.depthTreeList = 0

        def load(self, l):
            self.n = len(l)
            self.depthTreeList = (self.n - 1).bit_length()  # Level
            self.table.append(l)
            for curLevel in range(1, self.depthTreeList):
                l = []
                for i in range(self.n - (2 ** curLevel - 1)):
                    n1 = self.table[curLevel - 1][i]
                    n2 = self.table[curLevel - 1][i + (2 ** (curLevel - 1))]
                    if n1[0] < n2[0]:
                        l.append(n1)
                    else:
                        l.append(n2)
                self.table.append(l)

        def query(self, l, r):  # [l, r)
            diff = r - l
            if diff <= 0:
                raise
            if diff == 1:
                return self.table[0][l]
            level = (diff - 1).bit_length() - 1
            n1 = self.table[level][l]
            n2 = self.table[level][r - (2 ** level)]
            if n1[0] < n2[0]:
                return n1
            else:
                return n2

    def do():
        import sys
        input = sys.stdin.readline

        from bisect import bisect_left, bisect_right
        n = int(input())
        dat = []
        INF = 2**60
        zatsu = set()
        for i in range(n):
            num = i + 1
            a, b = map(int, input().split())
            a,b = min(a,b), max(a,b)
            zatsu.add(a)
            zatsu.add(b)
            dat.append([a, b, num])
        if n == 1:
            print("-1")
            return

        # 座標圧縮
        zatsu = list(zatsu)
        zatsu.sort()
        zatsu = list(enumerate(zatsu))
        zTable = dict()
        for i in range(len(zatsu)):
            zTable[zatsu[i][1]] = zatsu[i][0]
        sList = [[INF, -1] for i in range( len(zatsu))]
        # 座標圧縮に点を対応させるとともに、Sparse Tableに乗せるテーブルを作る
        for i in range(n):
            a,b,num = dat[i]
            a,b = zTable[a], zTable[b]
            dat[i][0] = a
            dat[i][1] = b
            if sList[a][0] > b:
                sList[a] = [b, num]
            if sList[b][0] > a:
                sList[b] = [a, num]

        st = sparseTable()
        st.load(sList)
        res = []

        # w, hを総当たりで、-1までの区間にもう一方より小さい点があるかを確認
        # あるなら、そのindexを答えとする
        for i in range(n):
            a,b,num = dat[i]
            xres = -1
            if a > 0:
                x = st.query(0, a)
                if x[0] != INF and x[0] < b:
                    xres = x[1]
            if b > 0:
                x = st.query(0, b)
                if x[0] != INF and x[0] < a:
                    xres = x[1]
            res.append(xres)
        print(" ".join(list(map(str, res))))

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
3
3 4
5 4
3 3
3
1 3
2 2
3 1
4
2 2
3 1
6 3
5 4
4
2 2
2 3
1 1
4 4"""
        output = """"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """1
2
3 9
1 6
"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()