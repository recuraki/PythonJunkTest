import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def do(s):
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                r += 1
            elif s[i] == ")":
                if r > 0:
                    r -= 1
                else:
                    l += 1
        #print(s, l, r)
        return (l,r)

    n = int(input())
    dat = []

    maxr = -1
    maxrind = 0
    maxrtotal = -1

    curl, curr = 0, 0
    for i in range(n):
        s = input()
        l ,r = do(s)
        if l != 0 or r != 0:
            dat.append( [l,r] )
            continue

    #print(curr, curl)
    dat.sort(key=lambda x: abs(x[0] - x[1]))
    #print(dat)

    for i in range(len(dat)):
        newl , newr = dat[i]
        #print("curl", curl, " curr", curr, " newl", newl, " newr", newr)
        caneraseL = min(curl, newr)
        caneraseR = min(curr, newl)
        if caneraseL == caneraseR:
            if curl > curr: # Lを消したい = newは左につける
                # 左につける ver00
                if curl >  newr: # いまのLの方が多いなら
                    curl, curr = newl + (curl - newr), curr
                else:
                    curl, curr = newl, curr + (newr - curl)
            else: # Rを消す = newは右につける
                # 右につける ver00
                if curr >  newl: # いまのRの方が多いなら
                    curl, curr = curl, newr + (curr - newl)
                else:
                    curl, curr = curl + (newl - curr), newr
        elif caneraseR > caneraseL:
            # 右につける ver00
            if curr > newl:  # いまのRの方が多いなら
                curl, curr = curl, newr + (curr - newl)
            else:
                curl, curr = curl + (newl - curr), newr
        else: # caneraseR < caneraseL
            # 左につける ver00
            if curl > newr:  # いまのLの方が多いなら
                curl, curr = newl + (curl - newr), curr
            else:
                curl, curr = newl, curr + (newr - curl)
    #print(curl,curr)
    print("Yes" if curl == curr == 0 else "No")

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_input_5(self):
        print("test_input_5")
        input = """5
)()((
))(
)(
(
)"""
        output = """No"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()