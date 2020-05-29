import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    from copy import deepcopy

    def do(idx, usedbuffer, s):
        #print("exec do idx={0}, s={1}, buf={2}".format(idx, s, usedbuffer))
        if idx == m:
            print(s)
            return True
        for nextcand in range(n):
            nextused = deepcopy(usedbuffer)
            isok = True
            for i in range(n):
                #print(" > check", i,n)
                if dat[i][idx] != dat[nextcand][idx]: # is not
                    #print(" > > diff ", dat[i][idx], dat[nextcand][idx])
                    if nextused[i] is True:
                        isok = False
                    nextused[i] = True

            if isok is False:
                continue

            # can go
            ret = do(idx + 1, nextused, s + dat[nextcand][idx])

            if ret is True:
                return True

        return False

    q = int(input())
    for _ in range(q):
        n, m = map(int, input().split())
        dat = []
        used = [False] * n
        for i in range(m):
            pass
        for i in range(n):
            s = input()
            dat.append(list(s))

        res = do(0, used, "")
        if res is False:
            print(-1)
        else:

           print("".join(list(map(str, dat))))







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
2 4
abac
zbab
2 4
aaaa
bbbb
3 3
baa
aaa
aab
2 2
ab
bb
3 1
a
b
c"""
        output = """abab
-1
aaa
ab
z"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()