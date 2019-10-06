import sys
from io import StringIO
import unittest

def resolve():
    s1,e1 = map(int, input().split())
    s2,e2 = map(int, input().split())
    s3,e3 = map(int, input().split())
    print(str(int(s1*e1/10 + s2*e2/10 + s3*e3/10  ) ))

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """50 7
40 8
30 9"""
        output = """94"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """990 10
990 10
990 10"""
        output = """2970"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()