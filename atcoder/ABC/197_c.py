import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def main():
        n = int(input())
        dat = list(map(int, input().split()))

        d = dict()

        def do(l, s, t):
            #print("do", l, s, t)
            if len(l) == 0:
                return [0]
            if len(l) == 1:
                return l
            if (s, t) in d:
                #print("hit", s, t)
                return d[s, t]
            ss = set()
            for i in range(1, len(l) + 1):
                ll = l[:i]
                ll2 = l[i:]
                curor = 0
                for x in ll:
                    curor |= x
                #print(ll, ll2, curor)
                res = do(ll2, i, t)
                #print(res)
                for x in res:
                    ss.add(curor ^ x)
            return ss

        ss = do(dat, 0, n - 1)
        print(min(list(ss)))



    main()

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
        input = """3
1 5 7"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
10 10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
1 3 3 1"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()