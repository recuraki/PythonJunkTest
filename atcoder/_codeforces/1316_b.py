import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def do(s, k):
        l = len(s)
        t = s
        k = k - 1
        if l % 2 == 0:
            if k % 2 == 0:
                return t[k:] + t[:k]
            else:
                return t[k:] + t[-l + k - 1: -l - 1: -1]
        else:
            if k % 2 == 1:
                return t[k:] + t[:k]
            else:
                return t[k:] + t[-l + k - 1: -l - 1: -1]
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        l = list(s)
        res = []
        #print(s)
        for i in range(1, n+1):
            res.append( (do(s, i), i) )
        res.sort()
        #print(res)
        print(res[0][0])
        print(res[0][1])





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
4
abab
6
qwerty
5
aaaaa
6
alaska
9
lfpbavjsm
1
p"""
        output = """abab
1
ertyqw
3
aaaaa
1
aksala
6
avjsmbpfl
5
p
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()