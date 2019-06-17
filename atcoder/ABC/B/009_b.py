import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    d = []
    for i in range(n):
        d.append(int(input()))
    d = list(set(d))
    d.sort()
    d.reverse()
    print(d[1])

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
100
200
300
300"""
        output = """200"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """5
50
370
819
433
120"""
        output = """433"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """6
100
100
100
200
200
200"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()