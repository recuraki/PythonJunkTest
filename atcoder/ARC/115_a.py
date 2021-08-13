import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    def do():
        n, m = map(int, input().split())
        dat = []
        cntodd = 0
        cnteven = 0
        for i in range(n):
            x = str(input())
            dat.append(x)
            if x.count("1") % 2 == 0:
                cnteven += 1
            else:
                cntodd += 1
        print(cntodd*cnteven)
        return

        dat.sort()
        print()
        print("\n".join(dat))
        for i in range(n):
            for j in range(i+1, n):
                can = True
                for pat in range(2<<(m-1)):
                    s = "{:05b}".format(pat)
                    #print(s, dat[i], dat[j])
                    scorei = scorej = 0
                    for k in range(m):
                        if s[k] == dat[i][k]:
                            scorei += 1
                        if s[k] == dat[j][k]:
                            scorej += 1
                    if scorei == scorej:
                        can = False
                        vi = int(dat[i], 2)
                        vj = int(dat[j], 2)
                        print("ng", dat[i], dat[j], bin(vi + vj), bin(vi ^ vj), bin(vi | vj), dat[i].count("1"), dat[j].count("1"))
                        break
                if can:
                    vi = int(dat[i],2)
                    vj = int(dat[j],2)
                    #print("ok", dat[i], dat[j], bin(vi+vj), bin(vi^vj), bin(vi|vj), dat[i].count("1"), dat[j].count("1"))

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
        input = """3 2
00
01
10"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7 5
10101
00001
00110
11110
00100
11111
10000"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()