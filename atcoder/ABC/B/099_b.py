import sys
from io import StringIO
import unittest

def resolve():
    a,b = map(int, input().split())
    diff = b-a
    r = (diff *( diff+1)) / 2
    print(int(r - b))

    """
0 1 2 3 4  5    
1 3 6 9 10 15
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
    def test_入力例_1(self):
        input = """8 13"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """54 65"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()