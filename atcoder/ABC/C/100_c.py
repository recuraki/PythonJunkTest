import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = list(map(int, input().split()))
    total = 0
    for i in range(n):
        x = dat_a[i]
        while True:
            if x % 2 == 1:
                break
            total += 1
            x = x // 2

    print(total)



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
        input = """3
5 2 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
631 577 243 199"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
2184 2126 1721 1800 1024 2528 3360 1945 1280 1776"""
        output = """39"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()