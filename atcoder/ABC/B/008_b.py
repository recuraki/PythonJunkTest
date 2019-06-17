import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    d = dict()
    import collections
    n = int(input())
    dat_d = []
    for i in range(n):
        dat_d.append(input())
    dat_c = collections.Counter(dat_d)
    print(dat_c.most_common()[0][0])



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """4
taro
jiro
taro
saburo"""
        output = """taro"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """1
takahashikun"""
        output = """takahashikun"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """9
a
b
c
c
b
c
b
d
e"""
        output = """b"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()