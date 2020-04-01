
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    odat = list(map(int, input().split()))
    dat = []
    for i in range(n):
        dat.append( [odat[i], i+1, 0] )
    #print(dat)
    dat.sort(reverse=True)
    for i in range(n):
        dat[i][2] = i + 1
    #print(dat)
    dat.sort(key=lambda x: x[0], reverse=True)
    for i in range(n):
        print(dat[i][1])

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input1(self):
        print("test_input1")
        input = """3
140 180 160"""
        output = """2
3
1"""
        self.assertIO(input, output)
    def test_input2(self):
        print("test_input2")
        input = """2
1000000000 1"""
        output = """1
2"""
        self.assertIO(input, output)
    def test_input3(self):
        print("test_input3")
        input = """8
3 1 4 15 9 2 6 5"""
        output = """4
5
7
8
3
1
6
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()