import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat_a = map(int, input().split())
    dat_a = list(dat_a)
    d1 = d2 = d4 = 0
    for i in range(n):
        if dat_a[i] % 4 == 0:
            d4 += 1
        elif dat_a[i] % 2 == 0:
            d2 += 1
        else:
            d1 += 1
    if d2 == 0:
        if d4 >= d1 - 1:
            print("Yes")
        else:
            print("No")
    else:
        if d4 >= d1:
            print("Yes")
        else:
            print("No")




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
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()