import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from copy import deepcopy
    q = int(input())
    for _ in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        sdat = deepcopy(dat)
        res = []
        for i in range(n):
            if i < (n//2):
                res.append(-dat[n-1-i])
            else:
                res.append(dat[n-1-i])
        print(" ".join(list(map(str, res))))
    # do()




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
2
1 100
4
1 2 3 6"""
        output = """-100 1
1 1 1 -1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()