import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    s = input()
    c1 = s.count("(")
    c2 = s.count(")")
    if c1 != c2:
        print(-1)
    else:
        need = [0] * n
        cnt = 0
        for i in range(n):
            if cnt < 0:
                need[i] = 1
            if s[i] == "(":
                cnt += 1
            elif s[i] == ")":
                cnt -= 1
            else:
                print("error")
            if cnt < 0:
                need[i] = 1
        #print(need)
        print(sum(need))




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
        input = """8
))((())("""
        output = """6"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
(()"""
        output = """-1"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()