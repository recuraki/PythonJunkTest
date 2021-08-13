import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        s = input()
        s = list(s)
        res = 0
        if len(s) == 1:
            print(0)
            return
        for i in range(len(s) - 2):
            cur = s[i]
            if s[i] == s[i + 1] == s[i + 2]:
                s[i + 1], s[i + 2] = i + 1, i + 2
                res += 2
                continue
            if s[i] == s[i + 2]:
                s[i + 2] = i + 2
                res += 1
                continue
            if s[i] == s[i + 1]:
                s[i + 1] = i + 1
                res += 1
                continue
        if s[-2] == s[-1]:
            s[-2] = len(s) - 2
            res += 1
        print(res)
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
        input = """7
babba
abaac
codeforces
zeroorez
abcdcba
bbbbbbb
a"""
        output = """1
1
0
1
1
4
0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """xxx"""
        output = """xxx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()