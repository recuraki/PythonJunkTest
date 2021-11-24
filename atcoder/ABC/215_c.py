import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        import itertools
        s, k = input().split()
        k = int(k)
        ss = set()
        for x in itertools.permutations(s):
            ss.add(x)
        ss = list(ss)
        ss.sort()
        print("".join(ss[k-1]))


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
        input = """aab 2"""
        output = """aba"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """baba 4"""
        output = """baab"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """ydxwacbz 40320"""
        output = """zyxwdcba"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()