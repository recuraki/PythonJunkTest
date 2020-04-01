import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    for _ in range(q):
        h, m = map(int, input().split())
        res = 0
        res += 60 * (23 - h)
        res += (60 - m)
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
        input = """5
23 55
23 0
0 1
4 20
23 59"""
        output = """5
60
1439
1180
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()