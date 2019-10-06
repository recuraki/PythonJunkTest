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
        input = """3 4
2 1 3
3 1 2 3
2 3 2"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 5
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 30
3 5 10 30"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()

def resolve():
    n,m = map(int, input().split())
    master = [True] * m
    for i in range(n):
        d = map(int, input().split())
        d = list(d)
        num = int(d[0])
        d = d[1:]
        table = [False] * (m + 1)
        for j in range(num):
            table[ d[j] - 1 ] = True
        for j in range(m):
            master[j] = master[j] and table[j]

    count = 0
    for j in range(m):
        if master[j]:
            count += 1
    print(count)