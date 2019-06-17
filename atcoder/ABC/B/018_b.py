import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    n = int(input())
    for i in range(n):
        l, r = map(int,input().split())
        s = s[:l-1] + "".join(reversed(list(s[l-1:r]))) + s[r:]
    print(s)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """abcdef
2
3 5
1 4"""
        output = """debacf"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """redcoat
3
1 7
1 2
3 4"""
        output = """atcoder"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()