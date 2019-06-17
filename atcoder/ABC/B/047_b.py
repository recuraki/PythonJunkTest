import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    w,h,n = map(int, input().split())
    x1,y1 = 0, 0
    x2, y2 = w, h
    for i in range(n):
        x,y,a = map(int, input().split())
        if a == 1:
            x1 = max(x1, x)
        elif a == 2:
            x2 = min(x2, x)
        elif a == 3:
            y1 = max(y1, y)
        elif a == 4:
            y2 = min(y2, y)
    #print("{0} {1} {2} {3}".format(str(x1), str(y1), str(x2), str(y2)))
    print(max((x2 - x1) * (y2 - y1), 0))


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
        input = """5 4 2
2 1 1
3 3 4"""
        output = """9"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 4 3
2 1 1
3 3 4
1 4 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 10 5
1 6 1
4 1 3
6 9 4
9 4 2
3 1 3"""
        output = """64"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()