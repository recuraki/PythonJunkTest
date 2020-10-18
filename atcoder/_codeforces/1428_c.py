import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import itertools

    def countstrs(s):
        return [(k, len(list(g))) for k, g in itertools.groupby(s)]

    def do():
        q = int(input())
        for _ in range(q):
            s = input()
            cntA, cntB = 0, 0
            for i in range(len(s)):
                if s[i] == "A":
                    cntA += 1
                else:
                    if cntA > 0:
                        cntA -= 1
                    else:
                        cntB += 1
            print(cntA + (cntB % 2))
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
        input = """4
AAA
BABA
AABBBABBBB
BAAABBAABBB"""
        output = """3
2
0
1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()