import sys
from io import StringIO
import unittest

def resolve():
    import math
    n = int(input())
    n = int(math.sqrt(n))
    n = pow(n, 2)
    print(n)
    """
    n = int(input())
    l = -1
    for i in range(100000):
        if n < i*i:
            print( (i - 1) * (i - 1) )
            break
    """
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
        input = """81"""
        output = """81"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """271828182"""
        output = """271821169"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()