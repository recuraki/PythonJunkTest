import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    qq = int(input())
    for q in range(qq):
        n, k = map(int, input().split())
        s = input()
        pos0 = []

        start0 = 0

        for i in range(n):
            if s[i] == "0":
                start0 += 1
                continue
            break

        s = s[start0:]
        n -= start0

        for i in range(n):
            if s[i] == "0":
                pos0.append(i)
        # print(pos0)
        cannum = 0
        target0 = -1
        moveto0 = -1

        for i in range(len(pos0)):
            if pos0[i] <= k:
                k -= pos0[i]
                cannum += 1
                continue
            else:
                target0 = pos0[i]
                moveto0 = pos0[i] - k
                break

        print("cannum:{0}, tar{1} mov{2}".format(cannum, target0, moveto0))
        res = []
        for i in range(start0):
            res.append("0")
        for i in range(cannum):
            res.append("0")
        count0 = 0
        for i in range(n):
            # print("i:{0}".format(i))
            # print("cur:" + "".join(res))
            if i == (moveto0 - cannum):
                # print("moveto0")
                res.append("0")
            if s[i] == "0":
                if count0 < cannum:
                    # print("count0 < cannum")
                    count0 += 1
                    continue
                elif i == target0:
                    # print("i == target0")
                    continue
                else:
                    # print("else")
                    res.append("0")
                    continue
            if s[i] == "1":
                # print("1")
                res.append("1")
                continue
        print("".join(res))



class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_input(self):
        print("test_input_123")
        input = """2
7 9
0000000
7 9
1111110"""
        output = """0000000
0111111"""
        self.assertIO(input, output)
    def test_input_1(self):
        print("test_input_1")
        input = """3
8 5
11011010
7 9
1111100
7 11
1111100"""
        output = """01011110
0101111
0011111"""
        self.assertIO(input, output)

    def test_input_12(self):
        print("test_input_12")
        input = """3
8 7
11110000
7 9
0001110
7 1
1111100"""
        output = """01011100
0000111
1111010"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()


