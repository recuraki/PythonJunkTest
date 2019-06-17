import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, m = map(int, input().split())
    dat_a = []
    dat_b = []
    for i in range(n):
        dat_a.append(input())
    for i in range(m):
        dat_b.append(input())
    if n == 1 and m == 1:
        if dat_a[0][0] == dat_b[0][0]:
            t = True
        else:
            t = False

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            t = True
            for k in range(m):
                print(dat_a[i + k][j:j+m])
                print(dat_b[k])
                if dat_a[i + k][j:j+m] != dat_b[k]:
                    t = False
                    break
            if t:
                break
        if t:
            break

    print("Yes" if t else "No")







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
        input = """3 2
#.#
.#.
#.#
#.
.#"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """4 1
....
....
....
....
#"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()