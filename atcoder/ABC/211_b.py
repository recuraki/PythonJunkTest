import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    s = set()
    s.add(input())
    s.add(input())
    s.add(input())
    s.add(input())
    print("Yes" if len(s) == 4 else "No")
    #dat = []
    #dat.append(input())
    #dat.append(input())
    #dat.append(input())
    #dat.append(input())
    #if "H" in dat and "2B" in dat and "3B" in dat and "HR" in dat:
    #    print("Yes")
    #else:
    #    print("No")


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
        input = """3B
HR
2B
H"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2B
3B
HR
3B"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()