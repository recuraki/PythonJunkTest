import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    #memo = {}
    import copy
    n = int(input())
    dat = map(int, input().split())
    dat = list(dat)

    def search(c, l):
        print("new search + {0}".format(l))
        if len(l) == 2:
            print("len2: {0} l = {1}".format(l[0] + l[1], l))
            return l[0] + l[1]
        if len(l) == 3:
            print("len3: {0} l = {1}".format(l[0] + l[1] + l[1] + l[2], l))
            return l[0] + l[1] + l[1] + l[2]

        m = 10000000000000
        for i in range(len(l) - 2):
            a = [dat[i] + dat[i + 1], dat[i + 1] + dat[i + 2]]
            print("c,a,p,s: {0},{1},{2},{3}".format(c,a, dat[:i],  dat[i + 3:]))
            newl = l[:i] + a + l[i + 3:]
            print("newl:{0}".format(newl))
            val = search(c+1, newl)
            m = min(m, val)

        print("RESSSS c={0} m={1} l={2}".format(c, m,l ))

        return m


    print(search(0, dat))



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