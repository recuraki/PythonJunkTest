import sys
from io import StringIO
import unittest

def resolve():
    count = 0
    n,m = map(int, input().split())
    sw = {}
    lt = {}
    for i in range(1, m+1):
        s = map(int, input().split())
        s = list(s)
        k = s[0]
        s = s[1:]
        lt[i] = s
        for j in range(k):
            t = sw.get(s[j], [])
            t.append(i)
            sw[s[j]] = t
    p = map(int, input().split())
    p = list(p)

    for i in range(pow(2, n)):
        sw_sta = [False] * (n + 1)
        for j in range(n):
            if (i & pow(2,j)) != 0:
                sw_sta[j + 1] = True
        allon = True
        for j in range(m):
            c = 0
            for k in lt[j + 1]:
                if sw_sta[k]:
                    c += 1
            if c % 2 != p[j]:
                allon = False
                break
        if allon:
            count += 1
    print(count)





class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()