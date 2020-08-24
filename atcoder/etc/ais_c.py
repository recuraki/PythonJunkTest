import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    res = [0] * 100001
    for x in range(1,110):
        for y in range(1,110):
            for z in range(1,110):
                v = x*x + y*y + z*z + x*y + y*z + x*z
                if v < 100001:
                    res[v] += 1
    for i in range(n):
        print(res[i+1])
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
        input = """20"""
        output = """0
0
0
0
0
1
0
0
0
0
3
0
0
0
0
0
3
3
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()