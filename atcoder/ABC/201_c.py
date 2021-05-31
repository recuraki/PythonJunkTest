import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    os = input()
    res = 0
    for i in range(10000):
        s = list(os) # 判定用の配列
        xx = "{:0>4}".format(i) # 1 -> 0001とかの文字にする
        can = True
        for x in xx: # 1桁ずつ見ていく
            x = int(x)
            if s[x] == "x":
                can = False
                break
            if s[x] == "o": # その数字があるなら
                s[x] = "?" # 使ったことにする(o以外にすればなんでもいい)
        if s.count("o") != 0: # "o"が残っているなら使っていないからダメ
            can = False
        if can:
            res += 1
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
        input = """ooo???xxxx"""
        output = """108"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """o?oo?oxoxo"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxxxx?xxxo"""
        output = """15"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()