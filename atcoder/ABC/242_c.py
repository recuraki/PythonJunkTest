import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    from functools import lru_cache


    def do():
        import sys
        import pprint
        sys.setrecursionlimit(1<<30)

        MOD = 998244353

        N = int(input())

        memo = [[-1 for _ in range(N + 1)] for i in range(10)]

        # pprint.pprint(memo)

        @lru_cache(maxsize=None)
        def dfs(x, length):
            #print(x, length)
            if length == 1:
                memo[x][length] = 1
                return 1
            elif memo[x][length] != -1:
                return memo[x][length]
            else:
                tmp = 0
                for next in range(-1,1 + 1):
                    if 1 <= next <= 9:
                        if memo[x][length] == -1:
                            tmp += dfs(next, length - 1)
                        else:
                            tmp += memo[x][length]
                        tmp %= MOD
                memo[x][length] = tmp
                return tmp

        ans = 0

        for i in range(1, 10):
            ans += dfs(i, N) % MOD

        ans = ans % MOD
        # pprint.pprint(memo)

        print(ans)

    # 1 time
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
        input = """4"""
        output = """203"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """25"""
        #self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000"""
        output = """248860093"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()