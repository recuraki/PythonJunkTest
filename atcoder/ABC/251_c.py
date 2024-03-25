import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    n = int(input())
    dat = list()
    known = set() # sを管理するリスト
    for i in range(n):
        s, t = input().split()
        if s in known: continue # sが既に出現したならスキップ
        known.add(s) # sを処理したと記録
        dat.append( (-int(t), i+1) ) # (-t, index)を作る
    dat.sort() # ソートして
    print(dat[0][1]) # 頭のindexを出力


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
aaa 10
bbb 20
aaa 30"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
aaa 9
bbb 10
ccc 10
ddd 10
bbb 11"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
bb 3
ba 1
aa 4
bb 1
ba 5
aa 9
aa 2
ab 6
bb 5
ab 3"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()