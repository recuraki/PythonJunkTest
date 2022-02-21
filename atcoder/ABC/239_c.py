import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    input = sys.stdin.readline
    from pprint import pprint

    import math
    INF = 1 << 63
    ceil = lambda a, b: (((a) + ((b) - 1)) // (b))

    def do():
        x1, y1, x2, y2 = map(int, input().split())
        def f(x, y):
            ans = set()
            ans.add( (x+ 2 , y + 1) )
            ans.add( (x+ 2 , y - 1) )
            ans.add( (x+ 1 , y + 2) )
            ans.add( (x+ 1 , y -2 ) )
            ans.add( (x- 2 , y + 1) )
            ans.add( (x- 2 , y - 1) )
            ans.add( (x- 1 , y + 2) )
            ans.add( (x- 1 , y -2 ) )
            return(ans)
        a = f(x1, y1)
        b = f(x2, y2)
        for x in a:
            if x in b:
                print("Yes")
                return
        print("No")



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
        input = """0 0 3 3"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """0 1 2 3"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1000000000 1000000000 999999999 999999999"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()