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
        an, su = map(int, input().split())
        if (an + an) > su:
            print("No")
            return
        if an | (su - an*2) == an ^ (su - an*2): print("Yes")
        else: print("No")

    # n questions
    q = int(input())
    for _ in range(q):
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
        input = """2
1 8
4 2"""
        output = """Yes
No"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758"""
        output = """No
Yes
Yes
No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()