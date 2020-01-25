import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    s = list(s)
    res = 0
    for i in range(n // 2):
        x = s[2*i + 0]
        y = s[2*i + 1]
        if x != y:
            continue
        elif x == "a" and y == "a":
            s[2 * i + 0] = "b"
            res += 1
        elif x == "b" and y == "b":
            s[2 * i + 0] = "a"
            res += 1
    print(res)
    print("".join(s))


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
bbbb"""
        output = """2
abba"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
ababab"""
        output = """0
ababab"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
aa"""
        output = """1
ba"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()