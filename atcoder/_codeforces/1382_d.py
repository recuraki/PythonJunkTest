import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        buf = []
        prev = dat[0]
        cnt = 1
        for i in range(1,n*2):
            #print(" > ", i, dat[i])
            if prev > dat[i]:
                cnt += 1
            else:
                buf.append(cnt)
                cnt = 1
                prev = dat[i]
        buf.append(cnt)
        #print(dat)
        #print(buf)

        dp = [None] * 20100
        for i in range(len(buf)):
            for j in range(2005, -1, -1):
                if dp[j] is None:
                    continue
                dp[j + buf[i]] = True
            dp[buf[i]] = True
        #print(dp[:20])
        if dp[n] is True:
            print("YES")
        else:
            print("NO")


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
        input = """6
2
2 3 1 4
2
3 1 2 4
4
3 2 6 1 5 7 8 4
3
1 2 3 4 5 6
4
6 1 3 7 4 5 8 2
6
4 3 2 5 1 11 9 12 8 6 10 7"""
        output = """YES
NO
YES
YES
NO
NO"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()