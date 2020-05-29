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
        can = False
        n,k = map(int, input().split())
        dat = [1] * k
        amari = n - (k)
        if amari % 2 == 0 and amari >= 0:
            if amari < 0:
                break
            can = True
            dat[0] += amari
            print("YES")
            print(" ".join(list(map(str, dat))))
            continue

        dat = [2] * k
        amari = n - (2 * k)
        if amari % 2 == 0 and amari >= 0:
            can = True
            dat[0] += amari
            print("YES")
            print(" ".join(list(map(str, dat))))
            continue

        print("NO")




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
        input = """8
10 3
100 4
8 7
97 2
8 8
3 10
5 3
1000000000 9"""
        output = """YES
4 2 4
YES
55 5 5 35
NO
NO
YES
1 1 1 1 1 1 1 1
NO
YES
3 1 1
YES
111111110 111111110 111111110 111111110 111111110 111111110 111111110 111111110 111111120"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()