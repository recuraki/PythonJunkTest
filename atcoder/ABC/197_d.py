import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import math
    n = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    x, y = (x1+x2)/2, (y1+y2)/2
    l = math.sqrt( (x1-x2)**2 + (y1-y2)**2 ) / 2
    xxx, yyy = (x1 - x), (y1 - y)
    deg = math.degrees(math.atan2(yyy, xxx) )
    rad = math.radians(deg + (360/n) )
    print(x + l * math.cos(rad), y + l * math.sin(rad))











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
1 1
2 2"""
        output = """2.00000000000 1.00000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
5 3
7 4"""
        output = """5.93301270189 2.38397459622"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()