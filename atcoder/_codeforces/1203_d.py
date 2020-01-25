
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    t = input()
    pos = 0
    ls = len(s)
    lt = len(t)
    def search(pos, indt, m):
        if indt >= lt:
            return 0
        if pos >= ls:
            return 0
        print("search pos={0}, indt={1}, m={2}".format(pos,indt,m))
        initpos = pos + 1
        while s.find(t[indt], pos) != -1:
            print(" while pos={0}, indt={1}, m={2}".format(pos, indt, m))
            next = s.find(t[indt], pos)
            print("find next={0}".format(next))
            leng = next - initpos
            print("leng1:{0}".format(leng))
            m = max(leng, m)
            leng = search(next + 1, indt + 1, m)
            print("leng2:{0}".format(leng))
            m = max(leng, m)
            pos = next + 1
        return m

    tmp = s.find(t[0])

    res = search(tmp, 0, 0)

    print(res)






class TestClass(unittest.TestCase):
    maxDiff = 100000
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
        input = """axxxxxb
ab"""
        output = """5"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """baaba
ab"""
        output = """2"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """abcde
abcde"""
        output = """0"""
        self.assertIO(input, output)


    def test_input_4(self):
        print("test_input_4")
        input = """asdfasdf
fasd"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()