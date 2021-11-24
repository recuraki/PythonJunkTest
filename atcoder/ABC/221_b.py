import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint


    INF = 1 << 63
    def do():
        s = input()
        t = input()
        if s == t:
            print("Yes")
            return
        l = list(s)
        for i in range(len(s) - 1):
            l[i], l[i+1] = l[i+1], l[i]
            x = "".join(l)
            #print(i, x)
            if t == "".join(l):
                print("Yes")
                return
            l[i], l[i+1] = l[i+1], l[i]
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
acb"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """aabb
bbaa"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """abcde
abcde"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()