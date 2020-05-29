import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n = int(input())
        #print("---")
        if n == 1:
            print(0)
        else:
            res = 0
            for i in range(0, ((n-1)//2)):
                c = i + 1
                res += c * ( (2*c -1) * 4 + 4)
                #print(c, (2*c - 1) * 4)
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
        input = """3
3
5
499993"""
        output = """8
40
41664916690999888"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()