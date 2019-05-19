import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    res = []
    while True:
        if n == 0:
            break
        if n > 7:
            n -= 8
            res.append(8)
        if n > 3:
            n -= 4
            res.append(4)
        if n > 1:
            n -= 2
            res.append(2)
        if n > 0:
            n -= 1
            res.append(1)
    print(len(res))
    for i in res:
        print(str(i))


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
        input = """5"""
        output = """3
1
2
2"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """1"""
        output = """1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()