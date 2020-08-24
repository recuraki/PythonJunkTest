import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    mod = 10**9 + 7
    def do():
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        buf = []
        nump, numm, numz = 0, 0, 0
        for i in range(n):
            if dat[i] == 0:
                numz += 1
            elif dat[i] > 0:
                nump += 1
                buf.append([dat[i], dat[i]])
            elif dat[i] < 0:
                numm += 1
                buf.append([dat[i], -dat[i]])
        if nump + numm < k:
            print(0)
            return
        dpmax = [1] * (k+10)
        dpmin = [1] * (k+10)
        buflen = len(buf)
        for i in range(buflen):
            if dat[i] > 0: # 正の場合
                for j in range(0, i+1):
                    dpmax[j+1] = max(dpmax[j+1], dpmax[j] * dat[i] % mod)
                    dpmax[j+1] = max(dpmax[j+1], dpmax[j] * dat[i] % mod)




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
        input = """4 2
1 2 -3 -4"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 3
-1 -2 -3 -4"""
        output = """1000000001"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 1
-1 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """10 10
1000000000 100000000 10000000 1000000 100000 10000 1000 100 10 1"""
        output = """999983200"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()