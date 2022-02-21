import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from pprint import pprint

    import math
    INF = 1 << 63

    class sparseTable(object):
        func = None
        depthTreeList: int = 0
        table = []

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
                    l.append(
                        self.func(self.table[curLevel - 1][i], self.table[curLevel - 1][i + (2 ** (curLevel - 1))]))
                self.table.append(l)

        def query(self, l, r):  # [l, r)
            diff = r - l
            if diff <= 0:
                raise
            if diff == 1:
                return self.table[0][l]
            level = (diff - 1).bit_length() - 1
            return self.func(self.table[level][l], self.table[level][r - (2 ** level)])

    class sparseTableMin(sparseTable):
        func = min


    def do():
        n = int(input())
        s = input()
        dat = []
        for i in range(n):
            x = s[i]
            dat.append( (ord(x) - ord("a"), -i) )
        st = sparseTableMin()
        st.load(dat)
        r = n-1
        #print(st.query(0, 4))
        for l in range(n): # l 文字目
            if l >= r: break # 超えてるなら無理
            curval, _ = dat[l]
            candval, ind = st.query(l+1, r + 1)
            ind = -ind
            if candval < curval: # swap is good
                dat[l], dat[ind] = dat[ind], dat[l]
                r = ind - 1

        ans = []
        #print(dat)
        for x, _ in dat:
            ans.append(chr(ord("a") + x))

        print("".join(ans))

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
dcab"""
        output = """acdb"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
ab"""
        output = """ab"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """16
cabaaabbbabcbaba"""
        output = """aaaaaaabbbbcbbbc"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """17
snwfpfwipeusiwkzo"""
        output = """effwpnwipsusiwkzo"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()