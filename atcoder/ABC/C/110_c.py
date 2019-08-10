import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    t = input()

    ds = dict()
    dt = dict()
    tr = dict()
    tr2 = dict()
    res = True
    for i in range(len(s)):
        ds[s[i]] = True
        dt[s[i]] = True
        if s[i] not in tr:
            tr[s[i]] = t[i]
        else:
            if tr[s[i]] != t[i]:
                res = False

        if t[i] not in tr2:
            tr2[t[i]] = s[i]
        else:
            if tr2[t[i]] != s[i]:
                res = False

    #if (len(ds) == 26 or len(dt) == 26) and ds != dt:
    #    res = False

    print("Yes" if res else "No")




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
        input = """azzel
apple"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """chokudai
redcoder"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()