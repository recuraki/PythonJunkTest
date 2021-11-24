import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    s = input()
    k = int(input())
    did = set()
    nextset = set()
    nextset.add(s)
    did.add(s)

    for loop in range(k):
        curset = nextset
        if len(curset) == 0: break
        nextset = set()
        for curs in curset:
            for i in range(len(s) - 1):
                l = list(curs)
                l[i], l[i+1] = l[i+1], l[i]
                news = "".join(l)
                if news in did: continue
                did.add(news)
                nextset.add(news)

    print(len(did))





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
        input = """KEY
1"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """KKEE
2"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """KKEEYY
11111111111111"""
        output = """90"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()