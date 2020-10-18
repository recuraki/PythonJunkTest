import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    t = input()
    res = 9099999999999
    ls , lt = len(s), len(t)
    for i in range(ls - lt + 1):
        cnt = 0
        for j in range(lt):
            if s[i + j]  == t[j]:
                pass
            else:
                cnt += 1
        res= min(res, cnt)
    print(res)


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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()