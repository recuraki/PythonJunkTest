import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():


    from pprint import pprint
    def do():
        n = int(input())
        dat1 = list(map(int, input().split()))
        dat2 = list(map(int, input().split()))
        dat3 = list(map(int, input().split()))
        dat1.sort()
        dat2.sort()
        dat3.sort()
        l2 = []
        j = 0
        for i in range(n):
            x = dat1[i]
            while j < len(dat2) and dat2[j] <= x:
                j += 1
            if j >= len(dat2): break
            l2.append(dat2[j])
            j += 1
        j = 0
        l3 = []
        for i in range(len(l2)):
            x = l2[i]
            while j < len(dat3) and dat3[j] <= x:
                j += 1
            if j >= len(dat3): break
            l3.append(dat3[j])
            j += 1
            if j >= len(dat3): break
        #print()
        #print(dat1)
        #print(l2)
        #print(l3)
        print(len(l3))
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
        input = """5
9 6 14 1 8
2 10 3 12 11
15 13 5 7 4"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """1
10
20
30"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
1 1 1
1 1 2
2 2 2"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()