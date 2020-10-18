import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, s = input().split()
    s = list(s)
    n = int(n)
    for i in range(n):
        if s[i] == "A":
            s[i] = 0
            continue
        if s[i] == "T":
            s[i] = 1
            continue
        if s[i] == "C":
            s[i] = 2
            continue
        if s[i] == "G":
            s[i] = 3
            continue
    n = int(n)
    datat = [0] * n
    datcg = [0] * n
    res = 0
    for i in range(n):
        buf = [0,0,0,0]
        for j in range(i, n):
            buf[s[j]] += 1
            if buf[0] == buf[1] and buf[2] == buf[3]:
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
        input = """4 AGCT"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 ATAT"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 AAATACCGCG"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()