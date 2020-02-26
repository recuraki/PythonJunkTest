import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a,b,c,d,e,f = 0,0,0,0,0,0
    n = int(input())
    for _ in range(n):
        x, y = map(float, input().split())
        if x >= 35:
            a+=1
        if 30 <= x < 35:
            b+=1
        if 25 <= x < 30:
            c += 1
        if 25 <= y:
            d += 1
        if y < 0 and x >= 0:
            e += 1
        if x < 0:
            f += 1
    print(a,b,c,d,e,f)


"""

熱帯夜：最低気温が 
25
 度以上の日
冬日　：最低気温が 
0
 度未満で、最高気温が 
0
 度以上の日
真冬日：最高気温が 
0
 度未満の日
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
    def test_input_1(self):
        print("test_input_1")
        input = """4
32.2 25.3
36.4 26.4
24.1 18.0
26.0 24.9"""
        output = """1 1 1 2 0 0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
-2 -5.2
2 -0.1
26.0 -0.1"""
        output = """0 0 1 0 2 1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
15.0 9.5
12.5 10.5
20.5 19.9
15.5 15.5"""
        output = """0 0 0 0 0 0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()