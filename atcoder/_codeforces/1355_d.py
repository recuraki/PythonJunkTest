import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n,s = map(int, input().split())
    res = [1] * n
    res[0] += (s-n)
    #print(res)
    k = s // 2
    if k > (n-1):
        print("YES")
        print(" ".join(list(map(str, res))))
        print(k)
    else:
        print("NO")


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
        input = """1 4"""
        output = """YES
4
2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4"""
        output = """NO"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 8"""
        output = """YES
6 1 1
4"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_3")
        input = """3 7"""
        output = """YES
5 1 1
3"""
        self.assertIO(input, output)

    def test_input_5(self):
        print("test_input_35")
        input = """4 7"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()