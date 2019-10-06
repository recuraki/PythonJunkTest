import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    import itertools
    keta = len(str(n))
    l = []
    for i in range(3,keta + 1):
        l = l + list(itertools.product([7,5,3], repeat = i))
    l = list(l)
    l = map(lambda x: "".join(list(map(str, x))), l)
    l = map(int, l)
    l = list(l)
    l = filter(lambda x: x <= n, l)
    l = filter(lambda x: str(x).find("3") != -1, l)
    l = filter(lambda x: str(x).find("5") != -1, l)
    l = filter(lambda x: str(x).find("7") != -1, l)
    l = list(l)
    print(len(l))

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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()