import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input().split()[0]
    ss = "b"
    res = 0
    end = False
    for i in range(100):
        if s == "b":
            end = True
            break

        res += 1
        ss = "a" + ss + "c"
        if ss == s:
            end = True
            break

        res += 1
        ss = "c" + ss + "a"
        if ss == s:
            end = True
            break

        res += 1
        ss = "b" + ss + "b"
        if ss == s:
            end = True
            break

    if end:
        print(res)
    else:
        print(-1)

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
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input4(self):
        print("test_input4")
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()