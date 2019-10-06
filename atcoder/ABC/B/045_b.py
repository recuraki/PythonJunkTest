import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    sa = input()
    sb = input()
    sc = input()
    t = "a"
    r = ""
    while True:
        if t == "a":
            if len(sa) == 0:
                r = "A"
                break
            t = sa[0]
            sa = sa[1:]
        elif t == "b":
            if len(sb) == 0:
                r = "B"
                break
            t = sb[0]
            sb = sb[1:]
        elif t == "c":
            if len(sc) == 0:
                r = "C"
                break
            t = sc[0]
            sc = sc[1:]
    print(r)

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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()