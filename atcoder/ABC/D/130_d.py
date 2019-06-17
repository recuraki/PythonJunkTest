import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    n, k = map(int, input().split())
    dat_a = list(map(int, input().split()))

    res = 0

    l = 0
    r = 0
    total = 0
    res = 0

    from pprint import pprint
    # pprint(dat_a)

    while l < n:
        #print("l={0}".format(l))
        while r < n:
            if total >= k:
                break
            #print("r={0}".format(r))
            total += dat_a[r]
            #print("total={0}".format(total))
            r += 1
        if total < k:
            break
        res += n - r + 1
        #print("add: {0}".format(str(n-r)))
        total -= dat_a[l]
        #print("total bext={0}".format(total))
        l += 1

    print(res)




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
        input = """4 10
6 1 2 7"""
        output = """2"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """3 5
3 3 3"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352"""
        output = """36"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()