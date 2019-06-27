import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())

    dat_h = list(map(int, input().split()))

    dat_map = []
    for i in range(n):
        dat_map.append([0] * 100)

    for i in range(n):
        for j in range(dat_h[i]):
            dat_map[i][j] = 1

    res = 0
    for i in range(100):
        cur = 0
        for j in range(n):
            if cur == 0:
                if dat_map[j][i] == 1:
                    res += 1
            cur = dat_map[j][i]

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
        input = """4
1 2 2 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
3 1 2 3 1"""
        output = """5"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """8
4 23 75 0 23 96 50 100"""
        output = """221"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()