import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    
    import sys
    #input = sys.stdin.readline
    from pprint import pprint
    import collections
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        d = collections.defaultdict(int)
        for x in dat:
            d[x] += 1
            if d[x] > 1:
                d[x] -= 1
                d[x+1] += 1

        print(len(d.keys()))

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
        input = """5
6
1 2 2 2 5 6
2
4 4
6
1 1 3 4 4 5
1
1
6
1 1 1 2 2 2"""
        output = """5
2
6
1
3"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()