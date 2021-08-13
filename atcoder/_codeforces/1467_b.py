import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    def do():
        n = int(input())
        buf = list(map(int, input().split()))
        dat = [-1] * (n + 4)
        for i in range(n):
            dat[i+2] = buf[i]
        dat[0] = dat[1] = buf[0]
        dat[n+2] = dat[n+3] = buf[n-1]
        cnt = 0
        if n in [1, 2, 3]:
            print(0)
            return
        # count
        for i in range(3, n +1):
            if dat[i - 1] < dat[i] and dat[i] > dat[i + 1]:
                cnt += 1
                continue
            if dat[i - 1] > dat[i] and dat[i] < dat[i + 1]:
                cnt += 1
                continue


        m = 0
        # print(dat)
        plist = [0, 0, 0, 0, 0]
        for i in range(3, n +1):
            #print(i)
            plist[0] = dat[i - 2]
            plist[1] = dat[i - 1]
            plist[2] = dat[i]
            plist[3] = dat[i + 1]
            plist[4] = dat[i + 2]

            t = 0
            if (plist[0] < plist[1] and plist[1] > plist[2]) or (plist[0] > plist[1] and plist[1] < plist[2]):
                t += 1
            if (plist[1] < plist[2] and plist[2] > plist[3]) or (plist[1] > plist[2] and plist[2] < plist[3]):
                t += 1
            if (plist[2] < plist[3] and plist[3] > plist[4]) or (plist[2] > plist[3] and plist[3] < plist[4]):
                t += 1
            orig= t

            plist[2] = dat[i - 1]
            t = 0
            if (plist[0] < plist[1] and plist[1] > plist[2]) or (plist[0] > plist[1] and plist[1] < plist[2]):
                t += 1
            if (plist[1] < plist[2] and plist[2] > plist[3]) or (plist[1] > plist[2] and plist[2] < plist[3]):
                t += 1
            if (plist[2] < plist[3] and plist[3] > plist[4]) or (plist[2] > plist[3] and plist[3] < plist[4]):
                t += 1
            m = max(m, orig - t)

            plist[2] = dat[i + 1]
            t = 0
            if (plist[0] < plist[1] and plist[1] > plist[2]) or (plist[0] > plist[1] and plist[1] < plist[2]):
                t += 1
            if (plist[1] < plist[2] and plist[2] > plist[3]) or (plist[1] > plist[2] and plist[2] < plist[3]):
                t += 1
            if (plist[2] < plist[3] and plist[3] > plist[4]) or (plist[2] > plist[3] and plist[3] < plist[4]):
                t += 1
            m = max(m, orig - t)

        print(cnt - m)

    q = int(input())
    for _ in range(q):
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
        input = """4
3
1 5 3
5
2 2 2 2 2
6
1 6 2 5 2 10
5
1 6 2 5 1"""
        output = """0
0
1
0"""
        self.assertIO(input, output)
    def test_input_12(self):
        print("test_input_12")
        input = """4
1
1
2
1 2
3
1 3 1
4
1 2 1 2
"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()