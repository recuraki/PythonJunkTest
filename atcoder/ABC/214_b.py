import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        s,t = map(int, input().split())
        res = 0
        for a in range(101):
            for b in range(101):
                for c in range(101):
                    if a+b+c <= s and a*b*c <= t:
                        res += 1
        print(res)

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
        input = """1 0"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 10"""
        output = """213"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """30 100"""
        output = """2471"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()