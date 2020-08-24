import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    k = int(input())
    x = 7 % k
    cnt = 0
    for i in range(2 * 10 ** 6):
        if x == 0:
            break
        x = (x * 10 + 7) % k
        cnt += 1
    if cnt == 2000000:
        print(-1)
    else:
        print(cnt + 1)



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
        input = """101"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """999983"""
        output = """999982"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """7"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()