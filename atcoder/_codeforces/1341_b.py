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
        peak = [0] * n
        for i in range(1, n - 1):
            if dat[i-1] < dat[i] and dat[i] > dat[i+1]:
                peak[i] += 1
        #print(peak)
        total = sum(peak[0:k])
        l, r = 0, k-1
        if peak[l] == 1:
            total -= 1
        if peak[r] == 1:
            total -= 1
        resl = l + 1
        resv = total
        #print(" total", total)

        for i in range(n-k):
            #print("l,r=",l,r, "res, {0} {1}".format(resv + 1, l))
            total -= peak[l + 1]
            l += 1
            r += 1
            total += peak[r - 1]
            #print(" total", total)
            if total > resv:
                #print("!")
                resv = total
                resl = l + 1
        print("{0} {1}".format(resv + 1, resl))




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
8 6
1 2 4 1 2 4 1 2
5 3
3 2 3 2 1
10 4
4 3 4 3 2 3 2 1 0 1
15 7
3 7 4 8 2 3 4 5 21 2 3 4 2 1 3
7 5
1 2 3 4 5 6 1"""
        output = """3 2
2 2
2 1
3 1
2 3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()