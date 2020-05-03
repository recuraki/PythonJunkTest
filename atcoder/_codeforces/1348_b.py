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
        n, k = map(int, input().split())
        dat = list(map(int, input().split()))
        dat = set(dat)
        if len(dat) > k:
            print(-1)
        else:
            dat = list(dat)
            dat.sort()
            fusoku = k - len(dat)
            cnt = 1
            while fusoku > 0:
                if cnt not in dat:
                    dat.append(cnt)
                    fusoku -= 1
                cnt += 1

            ll = 100
            print(ll)
            res = []
            for i in range(0, ll):
                res.append(dat[i % len(dat)])
            print(" ".join(list(map(str, res))))


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
        input = """1
3 2
3 2 1"""
        output = """5
1 2 1 2 1
4
1 2 2 1
-1
7
4 3 2 1 4 3 2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()