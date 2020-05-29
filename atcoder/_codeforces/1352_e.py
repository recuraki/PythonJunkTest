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
        tmp = set()
        n = int(input())
        dat = list(map(int, input().split()))
        used = dict()
        res = dict()
        for i in range(n):
            used[dat[i]] = True

        #print(used)

        for i in range(n):
            sum = dat[i]
            for j in range(i+1, n):
                sum += dat[j]
                tmp.add(sum)
                if sum in used:
                    res[sum] = True
        final = 0
        for i in range(n):
            if dat[i] in res:
                print(dat[i])
                final += 1
        print(tmp)
        print(final)





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
12
5 8 10 1 1 10 7 3 12 3 3 7"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()