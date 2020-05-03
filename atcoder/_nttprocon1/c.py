import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    a, b = map(int, input().split())
    dat = list(map(int, input().split()))
    dat = list(map(lambda x: x**2, dat))


    if len(dat) >= 2:
        print(dat)

        res = 0

        buf = []
        import collections
        for x in range(len(dat)):
            for y in range(x + 1, len(dat)):
                for z in range(y + 1, len(dat)):
                    #print("{0} {1} {2}".format(x,y,z))
                    if (dat[z] == dat[x] + dat[y]) :
                        res += 1
                    if (dat[x] == dat[y] + dat[z]):
                        res += 1
                    if (dat[y] == dat[x] + dat[z]):
                        res += 1

        for x in range(len(dat)):
            for y in range(x + 1, len(dat)):
                buf.append(dat[x] + dat[y])
                if (dat[x] - dat[y]) != 0:
                    buf.append(abs(dat[x] - dat[y]))
                if abs(dat[y] - dat[x]) != abs(dat[x] - dat[y]):
                    buf.append(abs(dat[y] - dat[x]))

        print(buf)
        c = collections.Counter(buf)

        print(b)
        print(c)
        ccount = c.most_common()[0][1]
        print("cc = {0}".format(ccount))
        if b <= ccount:
            res2 = ccount * b
        else:
            res2 = ccount * ccount


        print("res={0}".format(res))
        print("add={0}".format(res2))
        print(res + res2)
    else:
        print(0)



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
        input = """5 0
3 4 5 3 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 1
3 13 12 4"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3 2
5 6 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_4(self):
        print("test_input_4")
        input = """1 1
3"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """10 1
5 6 7 8 9 5 6 7 8 9"""
        output = """4"""
        self.assertIO(input, output)

    def test_input_6(self):
        print("test_input_6")
        input = """18 8
1 11 3 1 25 23 17 1 11 5 24 11 7 27 4 10 15 14"""
        output = """86"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()