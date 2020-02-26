import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n, m = map(int, input().split())
    s1 = s2 = sc = ""
    dat = []
    for _ in range(n):
        dat.append(input())

    while 0 < len(dat):
        s = dat[0]
        del dat[0]
        if sc == "": # 単独で回文かを判定
            if s == "".join(reversed(s)):
                sc = s
                continue
        # 残りに自分の反転文字列があればそれを採用
        for j in range(0, len(dat)):
            ss = "".join(reversed(dat[j]))
            if s == ss:
                s1 = s1 + s
                s2 = dat[j] + s2
                del dat[j] # 使った文字列は削除
                break # 1つ見つかればその先は探さない

    res = s1 + sc + s2
    print(len(res))
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
        input = """3 3
tab
one
bat"""
        output = """6
tabbat"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 2
oo
ox
xo
xx"""
        output = """6
oxxxxo"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 5
hello
codef
orces"""
        output = """0
"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """9 4
abab
baba
abcd
bcde
cdef
defg
wxyz
zyxw
ijji"""
        output = """20
ababwxyzijjizyxwbaba"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()