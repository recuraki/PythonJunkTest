import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    #import pypyjit
    #pypyjit.set_param('max_unroll_recursion=-1')
    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))
    def do():
        """
        dp[i][j]:
        i文字目であり得る文字で、
        j = 0: まだより若くなっていない
        j = 1: もう若くなった
        """
        mod = 998244353
        n = int(input())
        s = input()
        l = []
        for x in s:
            x = ord(x) - ord("A")
            l.append(x)

        # 最初の状態
        canuse = []
        for ind in range(0, n):
            j = n - 1 - ind # 対応する文字
            canuse.append(min(l[ind], l[j])) # この数字まで使える文字

        dp = [[0] * 2 for _ in range(26)]
        for i in range(canuse[0] + 1):
            if i < l[0]: dp[i][1] = 1
            else:        dp[i][0] = 1


        for ind in range(1, n):
            if n % 2 == 0:
                if ind >= (n//2): break
            else:
                if ind > (n//2):break

            print(ind)
            print(dp)

            newdp = [[0] * 2 for _ in range(26)]

            prev0 = prev1 = 0
            for i in range(26): # 前の文字の自由なやつと、束縛されている子
                prev0 += dp[i][0]
                prev1 += dp[i][1]
                prev0 %= mod
                prev1 %= mod

            # もう自由な場合の処理
            for i in range(26):
                newdp[i][1] += prev1 % mod # 自由なやつからきた奴
            # 拘束されている処理
            for i in range(canuse[ind] + 1):
                if i < l[ind]: # もし、この文字よりも小さい
                    newdp[i][1] += prev0 # もう若くなっているのは全部
                    newdp[i][1] %= mod
                elif i == l[ind]:
                    newdp[i][0] += prev0
                    newdp[i][0] %= mod
            dp = newdp

        ans = 0
        for i in range(26):
            for j in range(2):
                ans += dp[i][j]
                ans %= mod
        print(ans)

    q = int(input())
    for _ in range(q):
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

    def test_input_12(self):
        print("test_input_12")
        input = """5
3
AXA
6
ABCZAZ
30
QWERTYUIOPASDFGHJKLZXCVBNMQWER
28
JVIISNEOXHSNEAAENSHXOENSIIVJ
31
KVOHEEMSOZZASHENDIGOJRTJVMVSDWW"""
        output = """24
29
212370247
36523399
231364016"""
        self.assertIO(input, output)

    def test_input_1(self):
        print("test_input_12")
        input = """1
6
ABCZAZ
"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()