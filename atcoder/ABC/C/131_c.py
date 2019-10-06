import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def lcm(x, y):
        import fractions
        return (x * y) // fractions.gcd(x, y)
    a,b,c,d = map(int, input().split())
    import math
    res = b - a + 1
    #print(res)
    res -= b // c - (a-1) // c
    #print("!" + str(math.ceil(b / c) - math.ceil(a / c)))
    #print(res)
    res -= b // d - (a-1) // d
    #print("!" + str(math.ceil(b / d) - math.ceil(a // d)))
    #print(res)
    res += b // lcm(c, d) - (a-1) // lcm(c,d)
    #print("!" + str(math.ceil(b / lcm(c, d)) - math.ceil(a / lcm(c,d))))
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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()