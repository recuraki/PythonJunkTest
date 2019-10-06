import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    f = True
    history = []
    lw = None
    for i in range(n):
        w = input()
        if w in history:
            f = False
            break
        if lw is not None:
            if w[0] != lw:
                f = False
                break
        history.append(w)
        lw = w[-1]
    if f:
        print("Yes")
    else:
        print("No")




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
        input = """4
hoge
english
hoge
enigma"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """3
abc
arc
agc"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()