import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat = [-1] + dat
    res = []
    for i in range(1, n + 1):
        x = i
        x = dat[x]
        cnt = 1
        while x != i:
            cnt += 1
            x = dat[x]
        res.append(str(cnt))
    print(" ".join(res))



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
        input = """6
1 3 2 5 6 4"""
        output = """1 2 2 3 3 3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
3 2 1"""
        output = """2 1 2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """2
1 2"""
        output = """1 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()