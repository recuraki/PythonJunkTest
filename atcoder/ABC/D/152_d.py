import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = [[0] * 10 for _ in range(10)]
    for i in range(1, n+1):
        dat[int(str(i)[0])][int(str(i)[-1])] += 1
    res = sum([dat[a][b] * dat[b][a] for a in range(10) for b in range(10)])
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
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """200000"""
        output = """400000008"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()