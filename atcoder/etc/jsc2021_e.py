import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def f(s, l, isleft):
        isleft = True
        cnt = 0

        n = len(s)

        if l == 1 and n == 1:
            return (0, s)

        if l == 0:
            if n == 0:
                return (0, "")
            if n == 1:
                return (-1, "")
            can = True
            s = list(s)
            for i in range(n//2):
                if s[i] == "?" or s[n-1-i] == "?":
                    continue
                if s[i] != s[n-1-i]:
                    continue
                if isleft:
                    s[i] = "?"
                    s[n-1-i] = "?"
                cnt += 2
            #print("ret", cnt)
            return (cnt, "".join(s))

        if n % 2 == 0: # l + rev(l)
            a = list(s[:n//2])
            b = list(s[n//2:])
            if len(a)==0 or len(b)==0:
                #print("-1, a")
                return (-1, None)
            assert len(a) == len(b)

            #print("pat1", a,b)

            x, a = f("".join(a), l-1, True)
            y, b = f("".join(b), l-1, False)

            if x == -1 or y == -1:
                return -1, ""

            if b.count("?") > a.count("?"):
                isleft = False
            a = list(a)
            b = list(b)
            for i in range(len(a)):
                if a[i] == "?" or b[len(a) - 1 - i] == "?":
                    continue
                if a[i] == b[len(a) - 1 - i]:
                    continue
                cnt += 2
                a[i] = "?"
                b[len(a) - 1 - i] = "?"
            a = "".join(a)
            b = "".join(b)

            #print("ret", x+y+cnt)
            return (x + y + cnt, a+b)

        else:
            a = list(s[:n//2])
            b = list(s[n//2 + 1:])
            if len(a)==0 or len(b)==0:
                #print("-1, b")
                return (-1, None)
            c = s[n//2]
            assert len(a) == len(b)

            x, a = f("".join(a), l-1, True)
            y, b = f("".join(b), l-1, False)

            if x == -1 or y == -1:
                return -1, ""

            if b.count("?") > a.count("?"):
                isleft = False
            a = list(a)
            b = list(b)
            for i in range(len(a)):
                if a[i] == "?" or b[len(a) - 1 - i] == "?":
                    continue
                if a[i] == b[len(a) - 1 - i]:
                    continue
                cnt += 2
                a[i] = "?"
                b[len(a) - 1 - i] = "?"
            a = "".join(a)
            b = "".join(b)

            #print("ret", x+y+cnt)
            return (x + y + cnt, a+c+b)

    def do():
        nostr = "impossible"
        origk = int(input())
        origs = input()
        res,s  = f(origs, origk, True)
        if res == -1:
            print(nostr)
            return
        else:
            #s = list(s)
            s = list(s)
            for i in range(len(s)):
                if s[i] == "?":
                    s[i] = origs[i]
                    #print("try", s, f("".join(s), origk, True))
                    if f("".join(s), origk, True)[0] == 0:
                        #print("hit")
                        res -= 1
                        continue
                    s[i] = "?"
            print(res)

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
aabaaaabaa"""
        output = """0"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """2
aabaaaabaa"""
        output = """4"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """3
aabaaaabaa"""
        output = """impossible"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """5
aabaaaabaa"""
        output = """impossible"""
        self.assertIO(input, output)
    def test_input_5(self):
        print("test_input_5")
        input = """2
acaabcbababaaac"""
        output = """6"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()