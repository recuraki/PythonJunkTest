import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from random import sample
    import sys
    s = input().split()
    t = input().split()
    for i in range(100000):
        if s == t and i%2==0:
            print("Yes")
            sys.exit(0)
        i, j = sample([0,1,2], 2)
        s[i], s[j] = s[j], s[i] # 適当な2つをswap
    print("No")



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
        input = """R G B
R G B"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()