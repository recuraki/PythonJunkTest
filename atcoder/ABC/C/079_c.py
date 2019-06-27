import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    a,b,c,d = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    if a+b+c+d == 7:
        print("{0}+{1}+{2}+{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a+b+c-d == 7:
        print("{0}+{1}+{2}-{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a+b-c+d == 7:
        print("{0}+{1}-{2}+{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a-b+c+d == 7:
        print("{0}-{1}+{2}+{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a+b-c-d == 7:
        print("{0}+{1}-{2}-{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a - b + c - d == 7:
        print("{0}-{1}+{2}-{3}=7".format(str(a), str(b), str(c), str(d)))
    elif a-b-c+d == 7:
        print("{0}-{1}-{2}+{3}=7".format(str(a),str(b),str(c),str(d)))
    elif a-b-c-d == 7:
        print("{0}-{1}-{2}-{3}=7".format(str(a),str(b),str(c),str(d)))

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
        input = """1222"""
        output = """1+2+2+2=7"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0290"""
        output = """0-2+9+0=7"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3242"""
        output = """3+2+4-2=7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()