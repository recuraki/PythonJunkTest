import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    flag = 0
    f = True
    for i in range(len(s)):
        if s[i] == "h" and flag == 0:
            flag = 1
            continue
        if s[i] == "i" and flag == 1:
            flag = 0
            continue
        else:
            f = False
    if f is False or flag != 0:
        print("No")
    else:
        print("Yes")



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
        input = """hihi"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """hi"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """ahi"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()