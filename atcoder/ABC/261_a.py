
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    a, b, c, d = map(int, input().split())
    dat = [0] * 1000
    ans = 0
    for i in range(a, b+1):
        dat[i] += 1
    for i in range(c,d+1):
        dat[i] += 1
    for i in range(200):
        if dat[i] == 2: ans += 1
    ans -= 1
    ans = max(0, ans)
    print(ans)




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
        input = """0 3 1 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 1 4 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """0 3 3 7"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_31(self):
        print("test_input_3")
        input = """1 3 3 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_32(self):
        print("test_input_3")
        input = """1 4 3 5"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()