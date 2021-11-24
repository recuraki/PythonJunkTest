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
        dat = list(map(int, input().split()))
        s = ""
        for x in dat:
            s += chr(ord("a") + (x-1))
        print(s)


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
        input = """1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """abcdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 1 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26"""
        output = """bacdefghijklmnopqrstuvwxyz"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """5 11 12 16 25 17 18 1 7 10 4 23 20 3 2 24 26 19 14 9 6 22 8 13 15 21"""
        output = """eklpyqragjdwtcbxzsnifvhmou"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()