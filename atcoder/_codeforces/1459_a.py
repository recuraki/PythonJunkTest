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
        s1 = input()
        s2 = input()
        s1 = list(map(int, s1))
        s2 = list(map(int, s2))
        w1 = w2 = 0
        #print(s1)
        #print(s2)
        for i in range(n):
            if s1[i] > s2[i]:
                w1 += 1
            elif s1[i] < s2[i]:
                w2 += 1
            else:
                pass
        if w1 == w2:
            print("EQUAL")
            return
        if w1 > w2:
            print("RED")
            return
        if w1 < w2:
            print("BLUE")
            return


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
        input = """3
3
777
111
3
314
159
5
09281
09281"""
        output = """RED
BLUE
EQUAL"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()