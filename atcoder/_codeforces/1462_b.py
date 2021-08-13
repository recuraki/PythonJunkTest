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
        dat = []
        n = int(input())
        s = input()
        if s[0] + s[1] + s[2] + s[3] == "2020":
            print("YES")
            return
        if s[0] + s[1] + s[2] + s[-1] == "2020":
            print("YES")
            return
        if s[0] + s[1] + s[-2] + s[-1] == "2020":
            print("YES")
            return
        if s[0] + s[-3] + s[-2] + s[-1] == "2020":
            print("YES")
            return
        if s[-4] + s[-3] + s[-2] + s[-1] == "2020":
            print("YES")
            return
        print("NO")

    q = int(input())
    for _ in range(q):
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
        input = """6
8
20192020
8
22019020
4
2020
5
20002
6
729040
6
200200"""
        output = """YES
YES
YES
NO
NO
NO"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()