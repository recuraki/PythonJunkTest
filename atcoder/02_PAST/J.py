import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    buf = []
    for i in range(501):
        buf.append(None)
    lv = 0
    buf[lv] = ""
    for i in range(len(s)):
        if s[i] == "(":
            lv += 1
            buf[lv] = ""
            continue
        if s[i] == ")":
            buf[lv-1] += buf[lv] + buf[lv][::-1]
            lv -= 1
            continue
        buf[lv] += s[i]
    print(buf[0])



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
        input = """(ab)c"""
        output = """abbac"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """past"""
        output = """past"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """(d(abc)e)()"""
        output = """dabccbaeeabccbad"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()