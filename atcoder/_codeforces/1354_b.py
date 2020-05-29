import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys

    q = int(input())
    for _ in range(q):
        #print("-----------------")
        have = [0] * 3
        s = input()
        s = list(s)
        s = list(map(lambda x: int(x)-1, s))
        #print(s)
        sl = len(s)
        l, r = 0, 0
        res = 9999999999999999999999
        have[s[0]] = True
        while r <= sl:
            #print("[l,r]", l, r)
            #print(" > new have", have)
            if have[0] == 0 or have[1] == 0 or have[2] == 0:
                r += 1
                if r >= sl:
                    break
                #print(s[r])
                have[s[r]] += 1
            else:
                res = min(res, (r - l + 1))
                have[s[l]] -= 1
                l += 1
            #print(" > end have", have)
        print(res if res != 9999999999999999999999 else 0)




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
        input = """7
123
12222133333332
112233
332211
12121212
333333
31121"""
        output = """3
3
4
4
0
0
4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()