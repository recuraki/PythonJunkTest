import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63

    def do():

        n = int(input())
        dat = []
        for i in range(2 * n - 1):
            l = list(map(int, input().split()))
            dat.append(l)
        att = [False] * (2 * n)

        def f(buf, val):
            nokorinum = 0
            for i in range(2 * n):
                if buf[i] is False: nokorinum += (1 << i)
            if nokorinum == 0:
                return val
            ans = 0
            for i in range(2 * n):
                if att[i] is True: continue
                att[i] = True
                for j in range(i + 1, 2 * n):
                    if att[j] is True: continue
                    att[j] = True
                    ans = max(ans, f(att, val ^ dat[i][j - i - 1]))
                    att[j] = False
                att[i] = False
            return ans

        print(f(att, 0))

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
        input = """2
4 0 1
5 3
2"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
5"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
900606388 317329110 665451442 1045743214 260775845 726039763 57365372 741277060 944347467
369646735 642395945 599952146 86221147 523579390 591944369 911198494 695097136
138172503 571268336 111747377 595746631 934427285 840101927 757856472
655483844 580613112 445614713 607825444 252585196 725229185
827291247 105489451 58628521 1032791417 152042357
919691140 703307785 100772330 370415195
666350287 691977663 987658020
1039679956 218233643
70938785"""
        output = """1073289207"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()