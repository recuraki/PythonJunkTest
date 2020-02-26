import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def polyToTriangle(poly):
        for i in range(len(poly) - 2):
            yield poly[0], poly[i + 1], poly[i + 2]

    def areaTriangle(pointsTriangle):
        (x1, y1), (x2, y2), (x3, y3) = pointsTriangle
        return abs((x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1)) / 2

    def areaPoly(data):
        return sum(areaTriangle(tri) for tri in polyToTriangle(data))

    a1,a2,a3,a4,a5,a6 = map(int, input().split())
    print(areaPoly([ [a1,a2],[a3,a4],[a5,a6] ]))

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
        input = """1 0 3 0 2 5"""
        output = """5.0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """-1 -2 3 4 5 6"""
        output = """2.0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """298 520 903 520 4 663"""
        output = """43257.5"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()