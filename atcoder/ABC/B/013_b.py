import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    oa = int(input())
    ob = int(input())

    c1 = c2 = 0

    a , b = oa, ob
    for i in range(10):
        if a == b:
            break
        c1 += 1
        a = a + 1
        if a == 10:
            a = 0

    a , b = oa, ob
    for i in range(10):
        if a == b:
            break
        c2 += 1
        a = a - 1
        if a == -1:
            a = 9

    print(min(c1,c2))


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
6"""
        output = """2"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """6
4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """8
1"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()