import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    for i in range(n):
        # print("i", i)
        res = [0] * n
        if i != 0:
            res[n - i] += 1
        else:
            resstr = res
            resstr = list(map(lambda x: chr(ord("a") + x), res))
            print("".join(resstr))
            continue
        while res[n - i] == 1:
            m = 0
            p = True
            for k in range(n):
                if res[k] > m + 1:
                    p = False
                m = max(m,res[k])
            resstr = res
            resstr = list(map(lambda x: chr(ord("a") + x), res))
            if p:
                print("".join(resstr))
            res[-1] += 1
            for j in range(1, i):
                #print("verf", res[: n-j], "n-j", n-j)
                if res[n - j] > max(res[:n - j]) + 1:
                    res[n - j] = 0
                    res[n - j - 1] += 1
                    break
        continue
        resstr = list(map(lambda x: chr(ord("a") + x), res))
        print("".join(res))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
        self.maxDiff=1000000
    def test_input_1(self):
        print("test_input_1")
        input = """6"""
        output = """a"""
        self.maxDiff=1000000
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """aa
ab"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_2")
        input = """3"""
        output = """aaa
aab
abc"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_2")
        input = """4"""
        output = """aaaa
aab
abc"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()