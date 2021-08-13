import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        n = int(input())
        s = list(input())
        res = 0
        while len(s) != 0:
            print("new", s)
            l = 0
            can = False
            for r in range(1, len(s)):
                print(s[r], s[l])
                if s[r] != s[l]:
                    print("hit")
                    res += 1
                    s = s[r+1:]
                    can = True
                    break
            if can: continue
            print(-1)
            return
        print(res)
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
abba"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
aba"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
abc"""
        output = """"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()