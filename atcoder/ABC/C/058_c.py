import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # アルゴリズムイントロダクション 15.4 LCS
    # Longest Common Subsequenceをとり、以下を返す
    # b: 結果
    # c: そこまでのlongestのcount(内部用)
    def lcs_length(x, y):
        m, n = len(x), len(y)
        b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = '↖'
                elif c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "↑"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "←"
        return c, b

    # アルゴリズムイントロダクション 15.4 LCS
    # bを基にもともとのinput xから共通部分を抜き出す。
    def lcs_decode(b, X, i, j):
        import collections
        res = collections.deque([])
        while True:
            # print("i={0}, j={1} b={2}".format(i,j,b[i][j]))
            if i == 0 or j == 0:
                break
            if b[i][j] == '↖':
                res.appendleft(X[i - 1])
                i -= 1
                j -= 1
            elif b[i][j] == "↑":
                i -= 1
                continue
            else:
                j -= 1
                continue
        return res




    n = int(input())
    dat = []
    for _ in range(n):
        s = input()
        s = "".join(sorted(list(s)))
        dat.append(s)
    cs = dat[0]
    for i in range(1, n):
        c, b = lcs_length(cs, dat[i])
        cs = "".join(lcs_decode(b, cs, len(cs), len(dat[i])))
    print(cs)

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
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()