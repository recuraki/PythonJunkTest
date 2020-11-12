import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        import itertools

        def countstrs(s):
            return [(k, len(list(g))) for k, g in itertools.groupby(s)]
        n = int(input())
        s = input()
        c= countstrs(s)
        print(max(c)-1)


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
        input = """3
2
101010
4
0110
8
11101000"""
        output = """0
1
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()