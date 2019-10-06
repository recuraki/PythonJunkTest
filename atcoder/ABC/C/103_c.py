import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def lcm(x, y):
        import fractions
        return (x * y) // fractions.gcd(x, y)
    n = int(input())
    dat_a = list(map(int, input().split()))
    res = dat_a[0]
    for i in range(n):
        res = lcm(res, dat_a[i])
    res -= 1
    total = 0
    for i in range(n):
        total += res % dat_a[i]
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
        input = """3
3 4 6"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
7 46 11 20 11"""
        output = """90"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """7
994 518 941 851 647 2 581"""
        output = """4527"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()