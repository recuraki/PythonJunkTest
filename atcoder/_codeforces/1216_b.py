import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))
    dat_a = []
    for i in range(n):
        dat_a.append((dat[i], i + 1))
    dat_a.sort(reverse=True, key=lambda x: x[0])
    x = 0
    res = 0
    res_dat = []
    for i in range(n):
        res += 1 + (x * dat_a[i][0])
        res_dat.append(str(dat_a[i][1]))
        x += 1
    print(res)
    print(" ".join(res_dat))


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
20 10 20"""
        output = """43
1 3 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
10 10 10 10"""
        output = """64
2 1 4 3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
5 4 5 4 4 5"""
        output = """69
6 1 3 5 2 4"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """2
1 4"""
        output = """3
2 1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()