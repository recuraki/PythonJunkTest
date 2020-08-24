import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = ""
    n -= 1
    while True:
        print("loop n", n)
        ch = n % 26
        print("n, ch", n, ch)
        res += chr(ord("a") + ch)
        n -= ch
        if n == 0:
            break
        n = n // 26
        print("nextn", n)
    print(res[::-1])


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input_12(self):
        print("test_input_12")
        input = """702"""
        output = """zz"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """26"""
        output = """z"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)

    def test_input_311(self):
        print("test_input_311")
        input = """475254"""
        output = """zzzz"""
        self.assertIO(input, output)

    def test_input_31(self):
        print("test_input_31")
        input = """475255"""
        output = """aaaaa"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()