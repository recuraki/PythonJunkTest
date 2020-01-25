import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    import math
    for qq in range(q):
        q2 = int(input())
        dat = []
        c = []
        c.append([0,0,0,0,0,0,0,0,0,0,0])
        c.append([0,0,0,0,0,0,0,0,0,0,0])
        c.append([0,0,0,0,0,0,0,0,0,0,0])
        c.append([0,0,0,0,0,0,0,0,0,0,0])
        for qq2 in range(q2):
            s = input()
            dat.append(s)
            for i in range(4):
                c[i][int(s[i])] += 1
        #print(dat)
        #print(c)
        count = 0
        for n in range(q2):
            isexist = False
            for nn in range(q2):
                # 自分自身は確認しない
                if nn == n:
                    continue
                if dat[n] == dat[nn]:
                    isexist = True
            # もし、他とことなるなら気にしない
            if isexist == False:
                continue
            count += 1
            s = dat[n]
            for i in range(10):
                if c[0][i] == 0:
                    c[0][i] += 1
                    c[0][int(dat[n][0])] -= 1
                    dat[n] = str(i) + s[1] + s[2] + s[3]
        print(count)
        for i in range(len(dat)):
            print(dat[i])









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
        input = """3
2
1234
0600
2
1337
1337
4
3139
3139
3139
3139"""
        output = """0
1234
0600
1
1337
1237
3
3139
3138
3939
6139"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()

