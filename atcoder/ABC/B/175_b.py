import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat.sort()
    #import collections
    #c = list(collections.Counter(dat))
    #c.sort()
    #print(c)
    #l = len(c)
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j + 1, n):
                a,b,c = dat[i], dat[j], dat[k]
                if a == b or a == c or b == c:
                    continue
                if c < a+b:
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
        input = """5
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()