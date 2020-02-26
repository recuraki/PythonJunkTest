import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools
    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]
    def countstrs_withIndex(s):
        d = countstrs(s)
        r = []
        ind = 0
        for i in range(len(d)):
            r.append((d[i][0], d[i][1], ind))
            ind += d[i][1]
        return r

    q = int(input())
    for _ in range(q):
        inp = input().split()
        n = int(inp[0])
        s = inp[1]

        """
        制約: > > < > > <
        最短の例: 7 6 4 5 3 1 2
        最長の例: 3 2 1 6 5 4 7
        """
        # 最小LIS
        dat = [0] * n
        num, last = n, 0
        # 0文字目からなめる
        for i in range(n):
            # 文字列が最後までくる、あるいは、単調増加にできないなら、
            # (つまり、この区間は"<" = 単調増加をイメージしている)
            if i == n - 1 or s[i] == ">":
                # その区間をなるべく大きな数になるように埋める
                for j in range(i, last - 1, -1):
                    dat[j] = str(num)
                    num -= 1
                last = i + 1
        print(" ".join(dat))

        dat = [0] * n
        num, last = 1, 0
        for i in range(n):
            print(dat)
            if i == n - 1 or s[i] == "<":
                for j in range(i, last - 1, -1):
                    dat[j] = str(num)
                    num += 1
                last = i + 1
        print(" ".join(dat))

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
        input = """3
3 <<
7 >><>><
5 >>><"""
        output = """1 2 3
1 2 3
5 4 3 7 2 1 6
4 3 1 7 5 2 6
4 3 2 1 5
5 4 2 1 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()