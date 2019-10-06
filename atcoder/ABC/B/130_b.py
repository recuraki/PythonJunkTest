import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, x = map(int, input().split())
    dat_l = list(map(int, input().split()))
    cur = 0
    c = 0
    for i in range(n):
        cur += dat_l[i]
        if cur > x:
            break
        c += 1
    print(c+1)



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
        input = """3 6
3 4 5"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 9
3 3 3 3"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()