import sys
from io import StringIO
import unittest

def resolve():
    a,b = map(int, input().split())
    x = int(str(a) + str(b))
    f = False
    for i in range(1000):
        if x == (i*i):
            f = True
            break
    print("Yes" if f else "No")


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
        input = """1 21"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """100 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """12 10"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()