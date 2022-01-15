import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint

    import math
    INF = 1 << 63
    def do():
        s = input()
        t = input()
        l1 = []
        l2 = []
        for x in s: l1.append(ord(x) - ord("a"))
        for x in t: l2.append(ord(x) - ord("a"))
        for offset in range(27):
            can = True
            for i in range(len(s)):
                if ((l1[i] + offset) % 26) == l2[i]: continue
                can = False
                break
            if can:
                print("Yes")
                return
        print("No")


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
        input = """abc
ijk"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """z
a"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """ppq
qqp"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """atcoder
atcoder"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()