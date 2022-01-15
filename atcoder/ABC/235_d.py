import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def main():
        from collections import defaultdict
        from sys import exit

        a, N = map(int, input().split())

        dp = defaultdict(set)
        i, dp[0] = 0, set([N])

        visited = set()

        while 1 not in dp[i]:
            is_ops = False
            for n in dp[i]:
                nn, j = n, i
                while nn % a == 0:
                    nxt = nn // a
                    if nxt == 1:
                        print(j + 1)
                        return
                    if nxt in dp[j + 1]:
                        break
                    dp[j + 1].add(nxt)
                    visited.add(nxt)
                    nn = nxt
                    j += 1
                    if not is_ops:
                        is_ops = True
                sn = str(n)
                if n > 10:
                    for j in range(len(sn)):
                        nxt = int(sn[1:] + sn[0])
                        if len(str(nxt)) != len(sn):
                            continue
                        if i == 0 or (i - 1 >= 0 and nxt not in visited and nxt != N and nxt not in visited):
                            dp[i + j + 1].add(nxt)
                            visited.add(nxt)
                            is_ops = True
            if not is_ops:
                print(-1)
                return
            i += 1
        print(i)
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
        input = """3 72"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 5"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2 611"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()