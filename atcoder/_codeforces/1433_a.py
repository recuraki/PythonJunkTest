import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    #input = sys.stdin.readline
    from pprint import pprint
    import sys
    def do():
        n = int(input())
        x = n % 10
        res = (x - 1)*10
        if len(str(n)) == 1:
            res += 1
        if len(str(n)) == 2:
            res += 1+2
        if len(str(n)) == 3:
            res += 1+2+3
        if len(str(n)) == 4:
            res += 1+2+3+4
        print(res)

    q = int(input())
    for _ in range(q):
        do()
    # do()



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
        input = """4
22
9999
1
777"""
        output = """13
90
1
66"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()