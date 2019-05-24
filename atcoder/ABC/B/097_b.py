import sys
from io import StringIO
import unittest

def resolve():
    import math
    n = int(input())
    res = [1]
    last = -1
    for i in range(1, n):
        for c in range(2, n):
            num = pow(i, c)
            if num == last:
                break
            if num <= n:
                res.append(num)
            else:
                break
            c+= 1
            last = num
    print(max(res))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """10"""
        output = """9"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """999"""
        output = """961"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()