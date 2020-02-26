import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat = list(map(int, input().split()))

    dat2 = []
    m = -1
    #print(dat[:k])
    n = sum(dat[:k])
    dat2.append(n)
    m = n
    mind = 0
    for i in range(1, len(dat) - k ):
        #print("in/out")
        #print(dat[k+i])
        #print(dat[i])
        n += dat[k+i]
        n -= dat[i]
        dat2.append(n)
        if n > m:
            m = n
            mind = i + 1


    #print(dat2)
    #print(m)
    #print(mind)

    r = 0
    for i in range(mind, mind + k):

        r += (dat[i] + 1) / 2

    print(r)


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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()