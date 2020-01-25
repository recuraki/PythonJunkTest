import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    qq = int(input())
    for q in range(qq):
        n,m,k = map(int, input().split())
        dat = list(map(int, input().split()))
        #print("n{0}, m{1}, k{2}".format(n,m,k))
        #print(dat)
        can = True
        for i in range(n - 1):
            #print("[CUR] i = {0}".format(i))
            ne = dat[i + 1] - k
            ne = 0 if ne < 0 else ne
            #print("next need {0}".format(ne))
            if ne < dat[i]:
                m += dat[i] - ne
                #print("pickup {0} m={1}".format(dat[i]-ne, m))
            else:
                m -= ne - dat[i]
                #print("drop {0} m={1}".format(ne-dat[i], m))
                if m < 0:
                    #print("gameover")
                    can = False
        print("YES" if can else "NO")


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
        input = """1
1 9 9
0 4 7"""
        output = """YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()