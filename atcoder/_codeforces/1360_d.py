import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    input = sys.stdin.readline

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors

    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        l = make_divisors(n)
        l.sort(reverse=True)
        #print(l)
        for item in l:
            if k >= item:
                print(n // item)
                break


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
8 7
8 1
6 10
999999733 999999732
999999733 999999733"""
        output = """2
8
1
999999733
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()