import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from copy import deepcopy
    import bisect
    n = int(input())
    dat = list(map(int, input().split()))
    odat = deepcopy(dat)
    dat.sort()
    x1 = dat[len(dat) // 2 - 1]
    x2 = dat[len(dat) // 2]
    for i in range(n):
        c = odat[i]
        j = bisect.bisect_left(dat, c)
        if j < len(dat) // 2:
            print(x2)
        else:
            print(x1)




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
2 4 4 3"""
        output = """4
3
3
4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
1 2"""
        output = """2
1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """6
5 5 4 4 3 3"""
        output = """4
4
4
4
4
4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()