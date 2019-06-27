import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    n = int(input())
    dat_a = list(map(int, input().split()))
    dat_a_e = []
    dat_a_o = []
    for i in range(n//2):
        dat_a_e.append(dat_a[2*i])
        dat_a_o.append(dat_a[2*i+1])
    #print(dat_a_e)
    #print(dat_a_o)
    c_e = collections.Counter(dat_a_e).most_common(2)
    c_o = collections.Counter(dat_a_o).most_common(2)
    if len(c_e) == 1:
        c_e.append((0,0))
    if len(c_o) == 1:
        c_o.append((0,0))

    if c_o[0][0] != c_e[0][0]:
        print(n//2 - c_e[0][1] + n//2 - c_o[0][1])
    else:
        x = n//2 - c_e[0][1] + n//2 - c_o[1][1]
        y = n//2 - c_e[1][1] + n//2 - c_o[0][1]
        print(min(x, y))




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
3 1 3 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
105 119 105 119 105 119"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()