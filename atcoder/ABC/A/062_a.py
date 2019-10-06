import sys
from io import StringIO
import unittest

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
        input = """1 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 4"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()


def resolve():
    g1 =[1,3,5,7,8,10,12]
    g2 =[4,6,9,11]
    g3 = [2]
    x,y = map(int, input().split())
    if x== 2 and y == 2:
        print("Yes")
    elif x in g1 and y in g1:
        print("Yes")
    elif x in g2 and y in g2:
        print("Yes")
    else:
        print("No")