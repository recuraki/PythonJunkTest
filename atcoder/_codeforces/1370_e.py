import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do ():
        n = int(input())
        s = input()
        t = input()
        if s.count("1") != t.count("1") or s.count("0") != t.count("0"):
            print(-1)
            return
        dat = []
        cur = 0
        for i in range(n):
            if s[i] == t[i]: # same then skip
                pass
            elif s[i] == "1":
                cur += 1
            elif s[i] == "0":
                cur -= 1
            dat.append(cur)
        x = abs(max(dat))
        y = abs(min(dat))
        print(max(x,y))


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
        input = """6
010000
000001"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10
1111100000
0000011111"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
10101010
01010101"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10
1111100000
1111100001"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()