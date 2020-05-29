import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    q = int(input())
    for _ in range(q):
        n, m, a, b = map(int, input().split())
        if m%a != 0 or n % b != 0:
            print("NO")
            continue
        else:
            dat = []
            for i in range(n):
                x = i % (m // a)
                l = [0] * (a*x) + [1] * (a) + [0] * (m - (a * (x+1)))
                dat.append(l)
            #print(dat)
        iscan = True
        for i in range(n):
            x = dat[i].count(1)
            if x != a:
                iscan = False
        for i in range(m):
            res = 0
            for j in range(n):
                if dat[j][i] == 1:
                    res += 1
            if res != b:
                iscan = False
        if iscan is False:
            print("NO")
        else:
            print("YES")
            for i in range(n):
                print("".join(list(map(str, dat[i]))))


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
3 6 2 1
2 2 2 1
2 2 2 2
4 4 2 2
2 1 1 2"""
        output = """YES
010001
100100
001010
NO
YES
11
11
YES
1100
1100
0011
0011
YES
1
1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()