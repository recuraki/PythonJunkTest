import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline
    def do():
        n = int(input())
        dat = list(map(int, input().split()))
        mix = min(dat)
        res = 0
        for x in dat:
            if x > mix:
                res += 1
        print(res)

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
        input = """4
3
3 2 2
2
5 5
4
1 3 3 7
5
1 1 3 3 7"""
        output = """1
0
3
3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()