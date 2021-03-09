import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x = map(int, input().split())
    dat = list(map(int, input().split()))
    finalRes = 10 ** 20
    for loop in range(1, n+1):
        # dp [n個とって][あまりがn] の最大値
        dp = [[None] * loop  for _ in range(loop)]
        target = x % loop
        print("need amari, loop",loop,  target)
        dp[0][0] = 0
        dp[0][dat[0] % loop] = dat[0]
        for i in range(1, n):
            newdp = [[None] * loop for _ in range(loop)]
            for ll in range(loop):
                if dp[ll] != None:
                    if newdp[ll] == None and dp[ll] + dat[i]  <= x:
                        newdp[ll + (dat[i] % loop)] = dp[ll] + dat[i]
                    else:
                        if dp[ll] + dat[i] <= x:
                            newdp[ll + (dat[i] % loop)] = max(dp[ll] + dat[i], newdp[ll + (dat[i] % loop)])
        dp = newdp
        for i in range(loop):
            if (x - dp[i]) % loop == 0:
                finalRes = min(finalRes, (x - dp[i]))


    print(finalRes)





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
        input = """3 9999999999
3 6 8"""
        output = """4999999994"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1 1000000000000000000
1"""
        output = """999999999999999999"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()