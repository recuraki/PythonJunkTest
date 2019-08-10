import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    dat = []
    # 0 = R, L = 1
    mode = 0
    r = 0
    l = 0
    for i in range(len(s)):
        if mode == 0:
            if s[i] == "R":
                r += 1
            elif s[i] == "L":
                l += 1
                mode = 1
        elif mode == 1:
            if s[i] == "L":
                l += 1
            elif s[i] == "R":
                dat.append((r, l))
                mode = 0
                l = 0
                r = 1
    # 最後のLの処理
    dat.append((r, l))
    res = []
    for r,l in dat:
        t = r + l
        if t % 2 == 1:
            for i in range(r-1):
                res.append("0")
            if r %2 == 1:
                res.append(str(t//2+1))
                res.append(str(t//2))
            else:
                res.append(str(t // 2))
                res.append(str(t // 2+1))
            for i in range(l-1):
                res.append("0")
        else:
            for i in range(r-1):
                res.append("0")
            res.append(str(t//2))
            res.append(str(t//2))
            for i in range(l-1):
                res.append("0")
    print(" ".join(res))






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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()