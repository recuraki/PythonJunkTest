import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat_d = []
    for i in range(n):
        a,b = map(int, input().split())
        dat_d.append((a, b))
    dat_d.sort(key=lambda x: x[0])
    total = 0
    for i in range(m):
        if dat_d[i][1] >= m:
            #print("buy {0} sum {1}-hon".format(dat_d[i][0], m))
            total += dat_d[i][0] * m
            break
        else:
            #print("buy {0} sum {1}-hon".format(dat_d[i][0], dat_d[i][1]))
            total += dat_d[i][1] * dat_d[i][0]
            m -= dat_d[i][1]

    print(total)


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
        input = """2 5
4 9
2 4"""
        output = """12"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 30
6 18
2 5
3 10
7 9"""
        output = """130"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 100000
1000000000 100000"""
        output = """100000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()