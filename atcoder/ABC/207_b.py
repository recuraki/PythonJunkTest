import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    import sys
    input = sys.stdin.readline
    from pprint import pprint

    def do():
        INF = 10**20
        a,b,c,d = map(int, input().split())
        def f(turn):
            red = c * turn
            blue = a + b * turn
            if blue <= (red * d):
                return True
            return False
        l, h = INF
        while l <= h:
            mid = (l + h) // 2
            if f(mid):
                h = mid - 1
            else:
                l = mid + 1
        if l == INF or h == INF:
            print(-1)
            return
        if f(l):
            print(l)
            return
        print(h)

    do()


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
        input = """5 2 3 2"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 9 2 3"""
        output = """-1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()