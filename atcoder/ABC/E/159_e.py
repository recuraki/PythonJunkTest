import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    h, w, k = map(int, input().split())
    maze = []
    ts = []
    for _ in range(h):
        l = input()
        l = list(map(int, list(l)))
        #print(l)
        x = 0
        tmps = []
        for j in range(w):
            x += l[j]
            tmps.append(x)
        ts.append(tmps)
        maze.append(l)
    #pprint(maze)
    #pprint("--")
    #pprint(ts)

    bin_a = ["{:09b}".format(a) for a in range(0, 2 ** (h - 1))]

    res = 9999999
    for cutpat in bin_a:
        cutpat = cutpat[::-1]
        #print("cutpat", cutpat)
        cutsum = [0] * 10
        gr = [-1] * 10
        gr[0] = 0
        grnum = 0
        for i in range(1, h):
            if cutpat[i - 1] == "1":
                grnum += 1
            gr[i] = grnum
        #print("grlist", gr)

        firstFail = False

        cutcount = cutpat.count("1") # 縦の切った回数
        for i in range(w): # 進む
            #print(" do", i)
            for j in range(h):
                cutsum[ gr[j] ] += maze[j][i]
            #print(" res", cutsum)
            isFail = False
            for j in range(h):
                #print("  chk gr", j)
                if cutsum[j] > k:
                    #print("over! gr:", j)
                    isFail = True
                    if i == 0:
                        firstFail = True
            if isFail:
                #print("cut", i)
                cutcount += 1
                cutsum = [0] * 10
                for j in range(h):
                    cutsum[gr[j]] += maze[j][i]
                for j in range(h):
                    #print("  chk gr", j)
                    if cutsum[j] > k:
                        isFail = True
                        if i == 0:
                            firstFail = True

        if firstFail:
            continue

        res = min(res, cutcount)

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

    def test_input_3(self):
        print("test_input_3")
        input = """3 3 1
111
111
111"""
        output = """4"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()