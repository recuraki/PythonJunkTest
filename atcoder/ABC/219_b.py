import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    res = ""
    for x in t:
        if x == "1": res += s1
        if x == "2": res += s2
        if x == "3": res += s3
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
        input = """mari
to
zzo
1321"""
        output = """marizzotomari"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """abra
cad
abra
123"""
        output = """abracadabra"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """a
b
c
1"""
        output = """a"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()