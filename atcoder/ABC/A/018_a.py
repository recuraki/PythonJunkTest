import sys
from io import StringIO
import unittest

def resolve():
    a = int(input())
    b = int(input())
    c = int(input())
    r = [0] * 3
    if a == max(a,b,c):
        r[0] = 1
    if b == max(a,b,c):
        r[1] = 1
    if c == max(a,b,c):
        r[2] = 1
    if a == min(a,b,c):
        r[0] = 3
    if b == min(a,b,c):
        r[1] = 3
    if c == min(a,b,c):
        r[2] = 3
    for i in range(3):
        if r[i] == 0:
            r[i] = 2
    print(r[0])
    print(r[1])
    print(r[2])


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
        input = """12
18
11"""
        output = """2
1
3"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """10
20
30"""
        output = """3
2
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()