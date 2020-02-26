import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = map(int, input().split())
    dat = list(dat)

    count = 10
    while len(dat) != 2:
        #count -= 1
        #if count ==0:
        #    break
        #print(dat)
        tmp = []
        for i in range(1, len(dat) - 1):
            tmp.append( (dat[i-1] + dat[i] + dat[i+1]) )
        """
        index = -1
        m = 1000000000000000
        print("tmp: {0}".format(tmp))
        for i in range(len(tmp) ):
            if m > tmp[i]:
                m = tmp[i]
                index = i
        print("index {0}".format(index))
        a = [dat[index] + dat[index + 1], dat[index + 1] + dat[index + 2]]
        print("a: {0}".format(a))
        dat = dat[:index] + a + dat[index+3:]
        """
        index = -1
        m = 100000000000000
        for i in range(1, len(dat) - 1):
            if m > dat[i]:
                m = dat[i]
                index = i

        print("index {0}".format(index))
        a = [dat[index-1] + dat[index], dat[index] + dat[index + 1]]
        print("a: {0}".format(a))
        dat = dat[:index-1] + a + dat[index+2:]


    print(dat[0] + dat[1])




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
3 1 4 2"""
        output = """16"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """6
5 2 4 1 6 9"""
        output = """51"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
3 1 4 1 5 9 2 6 5 3"""
        output = """115"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()