import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():



    from pprint import pprint
    INF = 1 << 63
    def do():
        x = input()
        d = dict()
        for i in range(26):
            d[x[i]] = chr(ord("a") + i)
        #print(d)

        n = int(input())
        dat = []
        for _ in range(n):
            s = input()
            news = ""
            for i in range(len(s)):
                news += d[s[i]]
            dat.append( (news, s) )

        dat.sort(key=lambda x: x[0])
        #print(dat)
        for a,b in dat:
            print(b)


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
        input = """bacdefghijklmnopqrstuvwxzy
4
abx
bzz
bzy
caa"""
        output = """bzz
bzy
abx
caa"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """zyxwvutsrqponmlkjihgfedcba
5
a
ab
abc
ac
b"""
        output = """b
a
ac
ab
abc"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()