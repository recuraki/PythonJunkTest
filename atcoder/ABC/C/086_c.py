import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    n, k = map(int, input().split())
    dat_a = list(map(int,input().split()))
    d = collections.Counter(dat_a)
    r_num =  len(d)- k
    res = 0
    r = d.most_common()[::-1]
    for i in range(r_num):
        res += r[i][1]
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
        input = """5 2
1 1 2 2 5"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 4
1 1 2 2"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 3
5 1 3 2 4 1 1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()