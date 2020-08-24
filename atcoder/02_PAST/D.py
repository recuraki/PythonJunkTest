import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    n = len(s)
    res = set([])
    for i in range(len(s)):
        for j in range(1,4):
            if i+j > n:
                continue
            for pat in range(2 ** j):
                pats = "{0:010b}".format(pat)
                pats = pats[::-1]
                #print("pat", pat, pats)
                dat = ""
                for k in range(j):
                    if pats[k] == "1":
                        dat += s[i+k]
                    else:
                        dat += "."
                #print(" > dat", dat)
                res.add(dat)
    #print(res)
    print(len(res))

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
        input = """ab"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """aa"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """aabbaabb"""
        output = """33"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()