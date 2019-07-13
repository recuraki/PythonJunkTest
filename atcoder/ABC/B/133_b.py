import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n, d = map(int, input().split())
    dat_x = []
    for i in range(n):
        l = map(int, input().split())
        l = list(l)
        dat_x .append((l))
    res = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                break
            s = 0
            for k in range(d):
                s += (dat_x[i][k] - dat_x[j][k]) * (dat_x[i][k] - dat_x[j][k])
            #print(s)
            t = math.sqrt(s)
            if t.is_integer():
                #print("{0} {1}".format(i, j))
                res += 1
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
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()