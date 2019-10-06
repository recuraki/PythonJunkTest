import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    k = int(input())
    dat_x = map(int, input().split())
    dat_x = list(dat_x)
    res = 0
    for i in range(len(dat_x)):
        x = dat_x[i]
        res += min(x * 2, ((k - x) *2 ))
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
        logging.info("test_input_1")
        input = """1
10
2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        logging.info("test_input_2")
        input = """2
9
3 6"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_3(self):
        logging.info("test_input_3")
        input = """5
20
11 12 9 17 12"""
        output = """74"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()