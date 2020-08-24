import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    x = int(input())
    for a in range(-1000, 1000):
        can = False
        for b in range(-1000, 1000):
            if (a ** 5) - (b ** 5) == x:
                print(a, b)
                can = True
                break
        if can:
            break


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
        input = """0"""
        output = """0 0"""
        self.assertIO(input, output)

    def test_input_11(self):
        print("test_input_1")
        input = """-16806"""
        output = """1 7"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """16808"""
        output = """1 -7"""
        self.assertIO(input, output)

    def test_input_21(self):
        print("test_input_2")
        input = """-32767"""
        output = """1 8"""
        self.assertIO(input, output)

    def test_input_22(self):
        print("test_input_2")
        input = """32769"""
        output = """1 -8"""
        self.assertIO(input, output)

    def test_input_221(self):
        print("test_input_2")
        input = """64"""
        output = """2 -2"""
        self.assertIO(input, output)

    def test_input_2211(self):
        print("test_input_2 -211")
        input = """-211"""
        output = """2 3"""
        self.assertIO(input, output)

    def test_input_22111(self):
        print("test_input_2 275")
        input = """275"""
        output = """2 -3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()