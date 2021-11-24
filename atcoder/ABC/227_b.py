import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    n = int(input())
    dat = list(map(int, input().split()))
    ss = set([4*a*b + 3*a + 3*b for a in range(1,1001) for b in range(1,1001)])
    ans = 0
    for x in dat: ans += 1 if x not in ss else 0
    print(ans)


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
10 20 39"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
666 777 888 777 666"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()