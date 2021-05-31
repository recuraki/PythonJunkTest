import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 組み合わせ
    def ncr(n, r):
        import math
        # nCrのr>nは組み合わせが存在しないので0を返す
        # raiseすべきのこともあるかも
        if r > n:
            return 0
        return math.factorial(n) // ((math.factorial(n - r) * math.factorial(r)))


    n, m = map(int, input().split())
    buf = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        buf.append( [x, y, z] )
    buf.sort()
    total = 1
    for i in range(1, n+1):
        total *= i
    print(total)
    for i in range(m):
        x, y, z = buf[i]
        subtotal = 0
        for ii in range(z+1, n+1):
            subsubtotal = ncr(n - (y-1), ii)
            for i in range()
            subsubtotal
        print(subtotal)
        for j in range(i):
            xx,yy,zz = buf[j]
            for iii in range(zz + 1, n+1):
                subtotal -= ncr(n - min(y,yy), iii)
        total -= subtotal
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
        input = """3 1
2 2 1"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 2
3 3 2
4 4 3"""
        output = """90"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """18 0"""
        output = """6402373705728000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()