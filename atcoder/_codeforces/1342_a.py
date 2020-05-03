import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        x,y = map(int, input().split())
        a,b = map(int, input().split())
        res = 999999999999999999999999999

        # pat 1
        both = x
        kata = abs(y - x)
        v = both * b + kata * a
        #print(both, kata, v)
        res = min(res, v)


        # pat 2
        both = y
        kata = abs(x - y)
        v = both * b + kata * a
        #print(both, kata, v)
        res = min(res, v)

        # pat 3
        both = 0
        kata = abs(x) + abs(y)
        v = both * b + kata * a
        #print(both, kata, v)
        res = min(res, v)

        # pat4
        kata = abs(x-y)
        both = min(x,y)
        v = both * b + kata * a
        #print(both, kata, v)
        res = min(res, v)

        print(res)



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
1 3
391 555
0 0
9 4"""
        output = """1337
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()