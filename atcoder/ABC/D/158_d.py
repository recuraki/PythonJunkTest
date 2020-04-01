import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    s = input()
    qq = int(input())
    qs = []
    flag = True
    for i in range(qq):
        l = input().split()
        qs.append(l)
        if l[0] == "1":
            #print("pre")
            flag = not(flag)


    from collections import deque

    preflag = flag
    res = ""
    pre = deque([])
    suf = deque([])
    for i in range(qq-1, -1, -1):
        q = qs[i]
        if q[0] == "1":
            flag = not(flag)

        elif q[0] == "2":
            if q[1] == "1":
                if flag:
                    pre.append(q[2])
                else:
                    suf.appendleft(q[2])

            elif q[1] == "2":
                if flag:
                    suf.appendleft(q[2])
                else:
                    pre.append(q[2])

    #print(pre)
    #print(s)
    #print(suf)
    #print(preflag)
    if preflag:
        print("".join(pre) + s + "".join(suf))
    else:
        print("".join(suf)[::-1] + s[::-1] + "".join(pre)[::-1])

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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """abc
6
1
1
2 1 d
2 2 e
2 2 f
1"""
        output = """fecbad"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()