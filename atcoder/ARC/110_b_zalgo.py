import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    class zAlgorithm():
        def __init__(self, s):
            self.sdat = list(map(lambda x: ord(x), s))
            self.sl = len(s)
            self.res = [0] * self.sl
            self.res[0] = self.sl
            i, j = 1, 0
            while i < self.sl:
                while (i + j) < self.sl:
                    if self.sdat[j] != self.sdat[i + j]:
                        break
                    j += 1
                self.res[i] = j
                if (j == 0):
                    i += 1
                    continue
                k = 1
                while (i + k) < self.sl and (k + self.res[k] < j):
                    self.res[i + k] = self.res[k]
                    k += 1
                i += k
                j -= k
    def do():
        n = int(input())
        s = input()
        zres = zAlgorithm(s + "_" + ("110" * 200000))
        i = 0
        cnt1 = cnt2 = 0
        while i + n <= 600000:
            if i + n <= 300000:
                if zres.res[n+1 + i] >= n:
                    cnt1+=1
                    cnt2+=1
                    i += 1
                    continue
            if zres.res[n+1 + i] >= n:
                cnt2+=1
            i+=1
        print(cnt1 + (cnt2 - cnt1) * 99999)
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
1011"""
        output = """9999999999"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """22
1011011011011011011011"""
        output = """9999999993"""
        self.assertIO(input, output)
    def test_input_11(self):
        print("test_input_12")
        input = """1
1"""
        output = """9999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()