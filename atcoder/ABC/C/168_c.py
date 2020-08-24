import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    a,b,h,m = map(int, input().split())
    thetah = h * 30 + m * 0.5
    thetam = m * 6
    #print(thetah, thetam)
    #thetah = 90 - thetah
    #thetam = 90 - thetam
    radh = math.radians(thetah)
    radm = math.radians(thetam)
    #print(thetah, thetam)
    x1, y1 = a * math.sin(radh), a * math.cos(radh)
    x2, y2 = b * math.sin(radm), b * math.cos(radm)
    #print(x1, y1, x2, y2)
    print(math.sqrt( (x1-x2)**2 + (y1-y2) ** 2))


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()