import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    while True:
        a,b,c = map(int, input().split())
        if a==b==c==-1:
            break
        if a==-1 or b==-1:
            print("F")
            continue
        if a+b>=80:
            print("A")
            continue
        if 65<= a+b <80:
            print("B")
            continue
        if 50<= a+b <65:
            print("C")
            continue
        if 30<= a+b <50:
            if c >= 50:
                print("C")
                continue
            else:
                print("D")
                continue
        print("F")



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
        input = """40 42 -1
20 30 -1
0 2 -1
-1 -1 -1"""
        output = """A
C
F"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()