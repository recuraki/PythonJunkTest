import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        s = input()
        dat = list(s)
        for i in range(4):
            dat[i] = int(dat[i])
        if dat[0] == dat[1] == dat[2] == dat[3]:
            print("Weak")
            return
        weak = True
        for i in range(3):
            if dat[i+1] == (dat[i] + 1):
                continue
            if dat[i] == 9 and dat[i+1] == 0:
                continue
            weak = False
        if weak:
            print("Weak")
        else:
            print("Strong")
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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()