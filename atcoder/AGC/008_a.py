import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x, y = map(int, input().split())
    res = 99999999999999
    # そのまま
    c = y - x
    if c >= 0:
        res = min(res, c)

    # 最初に1かい押す
    c = y - (-x)
    if c >= 0:
        res = min(res, c + 1)

    # 最後に1かい押す
    c = (-y) - (x)
    if c >= 0:
        res = min(res, c + 1)

    # 2回押す
    c = (-y) - (-x)
    if c >= 0:
        res = min(res, c + 2)

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
        input = """10 20"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 -10"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """-10 -20"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_31")
        input = """-10 -10"""
        output = """0"""
        self.assertIO(input, output)

    def test_input_311(self):
        print("test_input_31")
        input = """5 -3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3111(self):
        print("test_input_31")
        input = """5 -7"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_31111(self):
        print("test_input_31")
        input = """-1 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_311111(self):
        print("test_input_31")
        input = """-2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3111111(self):
        print("test_input_31")
        input = """7 5"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_31111111(self):
        print("test_input_31")
        input = """-5 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_311111111(self):
        print("test_input_31")
        input = """0 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3111111111(self):
        print("test_input_31")
        input = """0 -3"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3112111111(self):
        print("test_input_31")
        input = """3 0"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_31111211111(self):
        print("test_input_31")
        input = """-3 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_input_31121111111(self):
        print("test_input_31")
        input = """-5 -3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_311112111111(self):
        print("test_input_31")
        input = """-5 -7"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()