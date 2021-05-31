import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def lcs(s1, s2):
        dp = []
        for s2_k in s2:
            bgn_idx = 0
            for i, cur_idx in enumerate(dp):
                chr_idx = s1.find(s2_k, bgn_idx) + 1
                if not chr_idx:
                    break
                dp[i] = min(cur_idx, chr_idx)
                bgn_idx = cur_idx
            else:
                chr_idx = s1.find(s2_k, bgn_idx) + 1
                if chr_idx:
                    dp.append(chr_idx)
        return len(dp)


    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    samenum = 0
    for i in range(lt):
        if s[i] == t[i]:
            samenum += 1
    #print(samenum)

    finalmax = samenum
    for i in range(1, ls - lt + 1):
        print("---")
        res = lcs(s[i:i+lt], t)
        finalmax = max(finalmax, res)
    print(lt - finalmax)

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
        input = """0001
101"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0101010
1010101"""
        output = """7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10101000010011011110
0010011111"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()