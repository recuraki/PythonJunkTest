import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    def do():
        a,b,c,d,e,f,x = map(int, input().split())
        kyoria = kyorib = 0

        kyoria += b * (x // (a+c)) * a
        nokoria = x % (a+c)
        #print(kyoria, nokoria)
        kyoria += b * (min(nokoria, a))
        #print(kyoria, nokoria)

        kyorib += e * (x // (d+f)) * d
        nokorib = x % (d+f)
        kyorib += e * (min(nokorib, d))
        #print(kyoria, kyorib)

        if kyoria == kyorib:
            print("Draw")
            return
        if kyoria > kyorib:
            print("Takahashi")
            return
        print("Aoki")
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
        input = """4 3 3 6 2 5 10"""
        output = """Takahashi"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 1 4 1 5 9 2"""
        output = """Aoki"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """1 1 1 1 1 1 1"""
        output = """Draw"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()