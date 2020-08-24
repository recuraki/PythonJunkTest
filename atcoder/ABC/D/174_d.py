import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do():
        if s.find("W") == -1:
            print(0)
            return
        c1 = s.count("W")
        c2 = s.count("R")
        c3 = 0
        l = 0
        r = len(s) - 1
        ll = len(s)
        while l < r and r >= 0 and l <= (ll-1):
            #print(l, r)
            if s[l] == "R":
                l += 1
                continue
            if s[r] == "W":
                r -= 1
                continue
            #print("c3+", l, r)
            c3 += 1
            l += 1
            r -= 1
        #print(c1,c2,c3)
        print(min(c1,c2,c3))


    n = int(input())
    s = input()
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
WWRR"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
RR"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
WRWWRWRR"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()