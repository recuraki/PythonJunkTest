import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, h = map(int, input().split())
    dat = []
    dat1 = []
    dat2 = []
    for i in range(n):
        a,b = map(int, input().split())
        dat.append( [a,b,i])
        dat1.append( [a, i] )
        dat2.append( [b, i] )

    dat1.sort(reverse=True)
    dat2.sort(reverse=True)

    #print(dat1)
    #print(dat2)

    normax = dat1[0][0]
    count = 0
    for i in range(n):
        #print("special" + str(dat2[i][0]))
        if dat2[i][0] > normax:
            count = count + 1
            h = h - dat2[i][0]
        if h <= 0:
            break
            #print("special" + str(dat2[i][0]))
    #print(h)
    if h > 0:
        import math
        count = count + math.ceil(h / normax)
    print(count)


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
        input = """1 10
3 5"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2 10
3 5
2 6"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        output = """860000004"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        output = """9"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()