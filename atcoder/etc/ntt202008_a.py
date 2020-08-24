import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b  = map(int, input().split())
    res = 0
    for i in range(a, b):
        x = i
        y = i + 1
        #print(x , y)
        if 0 <= x <= 5 and 0 <= y <= 5:
            res += 1
            #print("hit1")
            continue
        if 22 <= x <= 29 and 22 <= y <= 29:
            res += 1
            #print("hit2")
            continue
        if 46 <= x <= 50 and 46 <= y <= 50:
            res += 1
            #print("hit2")
            continue

    print(res)






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
        input = """13 24"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 26"""
        output = """6"""
        self.assertIO(input, output)
    def test_input_21(self):
        print("test_input_21")
        input = """0 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_211(self):
        print("test_input_211")
        input = """5 6"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2111(self):
        print("test_input_2111")
        input = """29 30"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_21111(self):
        print("test_input_21111")
        input = """28 29"""
        output = """1"""
        self.assertIO(input, output)

    def test_input_21111(self):
        print("test_input_21111")
        input = """28 29"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_211111(self):
        print("test_input_211111")
        input = """30 46"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_211111(self):
        print("test_input_211111")
        input = """30 48"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()