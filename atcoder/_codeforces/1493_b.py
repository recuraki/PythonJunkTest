import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():

    def do():
        conv = dict()
        conv["0"] = "0"
        conv["1"] = "1"
        conv["2"] = "5"
        conv["3"] = "xxxxxx"
        conv["4"] = "xxxxxx"
        conv["5"] = "2"
        conv["6"] = "xxxxxx"
        conv["7"] = "xxxxxx"
        conv["8"] = "8"
        conv["9"] = "xxxxxx"


        def isitok(curtime):
            curtime %= maxtime
            h, m = curtime // maxm, curtime % maxm
            #print(h, m)
            hstr = "{:02}".format(h)
            mstr = "{:02}".format(m)
            newm = conv[hstr[1]] + conv[hstr[0]]
            newh = conv[mstr[1]] + conv[mstr[0]]
            #print(newh, newh)
            if newm.find("x") != -1 or newh.find("x") != -1:
                return False
            if int(newh) >= maxh or int(newm) >= maxm:
                return False
            return True



        maxh, maxm = map(int, input().split())
        s = input().split(":")
        h, m = int(s[0]), int(s[1])
        curtime = (maxm * h) + m
        maxtime = maxh * maxm
        #print(curtime, maxtime)
        while True:
            if isitok(curtime):
                h, m = curtime // maxm, curtime % maxm
                print("{:02}".format(h)+":"+"{:02}".format(m))
                break
            curtime += 1
            curtime %= maxtime

    q = int(input())
    for _ in range(q):
        do()
        #print("--")


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
24 60
12:21
24 60
23:59
90 80
52:26
1 100
00:01
10 10
04:04"""
        output = """12:21
00:00
52:28
00:00
00:00"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()