import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = []
    import fractions

    for i in range(n):
        a, b = map(int, input().split())
        c = fractions.gcd(a, b)
        #a, b = a // c, b // c # 約分する
        dat.append( (a, b) )

    a, b = 1, 1

    import math
    for i in range(n):
        x, y = dat[i]
        c = max( (a + x - 1) // x, (b + y - 1) // y)
        #print("{0},{1}: c= {4} : {2},{3}".format(x, y, a,b,c))
        a, b = x * c, y * c
    print(a + b)



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
2 3
1 1
3 2"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
1 1
1 1
1 5
1 100"""
        output = """101"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5
3 10
48 17
31 199
231 23
3 2"""
        output = """6930"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()