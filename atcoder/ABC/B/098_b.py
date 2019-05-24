import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    s = input()
    mc = 0
    mindex = -1
    for i in range(1, len(s)):
        a = {}
        b = {}
        sa = s[0:i]
        sb = s[i:]
        c = 0
        for x in range(len(sa)):
            a[sa[x]] = True
        for x in range(len(sb)):
            b[sb[x]] = True
        for j in a.keys():
            if j in b:
                c += 1
        if mc < c:
            mc = c
            mindex = i
    print(mc)




class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """6
aabbca"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """10
aaaaaaaaaa"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()