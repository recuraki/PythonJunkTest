import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    n, m = map(int, input().split())
    dat = list(map(int, input().split()))
    dat.reverse()
    used = dict()
    res = []
    for i in range(len(dat)):
        if dat[i] not in used:
            res.append(dat[i])
            used[dat[i]] = True
    print(" ".join(list(map(str, res))))


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
        input = """3 5
2 4 1"""
        output = """1 4 2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6 5
2 4 1 4 5 2"""
        output = """2 5 4 1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 8
3 3 3 3 3 3 3 3 3 3"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()