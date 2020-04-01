import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import sys
    calcLower2Index = lambda x: ord(x) - ord("a")
    calcUpper2Index = lambda x: ord(x) - ord("A")
    calcIndex2Lower = lambda x: chr(ord("a") + x)
    calcIndex2Upper = lambda x: chr(ord("A") + x)
    s = input()
    f = [False] * 26
    l = len(s)
    if  l == 26: #full
        res = []
        if s == "zyxwvutsrqponmlkjihgfedcba":
            print(-1)
        else:
            m = -1 # これまでのmax
            ind = -1
            endf = False
            for i in range(l):
                ch = calcLower2Index(s[i])
                f[ch] = True
                ind += 1
                if m > ch:
                    for k in range(26):
                        if f[k] is False:
                            t = k
                            break
                    res[-2] = calcIndex2Lower(t)
                    print("".join(res[:-1]))
                    endf = True
                    break
                else:
                    m = ch
                    res.append(calcIndex2Lower(ch))
                if endf:
                    break

    else: # under 26
        for i in range(l):
            c = calcLower2Index(s[i])
            f[c] = True
        can = ""
        for i in range(26):
            if f[i] is False:
                can = calcIndex2Lower(i)
                break
        print(s + can)


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
        input = """atcoder"""
        output = """atcoderb"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """abc"""
        output = """abcd"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """zyxwvutsrqponmlkjihgfedcba"""
        output = """-1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """abcdefghijklmnopqrstuvwzyx"""
        output = """abcdefghijklmnopqrstuvx"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()