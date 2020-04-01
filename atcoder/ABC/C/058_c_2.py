import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = ""
    dat = []
    n = int(input())
    for _ in range(n):
        dat.append(input())
    for i in range(26):
        tch = chr(ord("a") + i)
        num = 99999
        for j in range(len(dat)):
            num = min(num, dat[j].count(tch))
        s += tch * num
    print(s)



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
cbaa
daacc
acacac"""
        output = """aac"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3
a
aa
b"""
        output = """"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()