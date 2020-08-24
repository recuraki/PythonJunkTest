import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n = int(input())
    dat = list(map(int, input().split()))

    import collections
    buf = collections.Counter(dat)
    dat = []
    dat = list(buf.keys())

    dat.sort()

    res = 0

    used = [False] * (1000100)

    for i in range(len(dat)):
        ok = True

        if used[dat[i]]:
            ok = False
        if buf[dat[i]] != 1:
            ok = False

        c = 0
        v = -1
        while True:
            c += 1
            v = dat[i] * c
            if v > 1000010:
                break
            used[v] = True

        used[dat[i]] = True

        if ok:
            res += 1
    #print(used[:10])
    print(res)



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
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_34(self):
        print("test_input_34")
        input = """10
33 18 45 28 8 19 89 86 2 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_341(self):
        print("test_input_341")
        input = """2
2 3"""
        output = """2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()