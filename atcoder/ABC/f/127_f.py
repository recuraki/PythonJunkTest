import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())
    history = []
    mi = 10000000000
    a = None
    b = 0
    for i in range(n):
        s = input()
        if s == "2":
            sum = b
            history.sort()
            if len(history) > 0:
                x = history[int(len(history) / 2) - 1]
            else:
                x = a
            for i in range(len(history)):
                sum += (abs(x - history[i]))
            print("{0} {1}".format(str(x), str(sum)))
        else:
            tra, a_in, b_in = map(int, s.split())
            history.append(a_in)
            b = b_in + b

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
        input = """4
1 4 2
2
1 1 -8
2"""
        output = """4 2
1 -3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
1 -1000000000 1000000000
1 -1000000000 1000000000
1 -1000000000 1000000000
2"""
        output = """-1000000000 3000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()