import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    t = [["000"],
         ["001"],
         ["00"]]
    for _ in range(q):
        dat = list(map(int, input().split()))
        dat = list(map(lambda x: 4 if x > 3 else x, dat))
        dat = list(map(str, dat))
        dat.sort()
        s = "".join(dat)
        print(s)





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
        input = """7
1 2 1
0 0 0
9 1 7
2 2 3
2 3 2
3 2 2
4 4 4"""
        output = """3
0
4
5
5
5
7"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()