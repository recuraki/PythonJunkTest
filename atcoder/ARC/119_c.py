import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    import collections
    prevcnt = collections.defaultdict(int)
    totalcnt = collections.defaultdict(int)
    n = int(input())
    dat = map(int, input().split())
    dat = list(dat)
    for i in range(n):
        if i%2 == 1:
            dat[i] = - dat[i]
    buf = [0] * n
    total = 0
    for i in range(n):
        total += dat[i]
        buf[i] = total

        totalcnt[total] += 1
    res = 0
    for i in range(n):
        x = buf[i]
        totalcnt[x] -= 1
        res += totalcnt[x]

    res += buf.count(0)
    print(res)
    #print(totalcnt)





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
5 8 8 6 6"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """7
12 8 11 3 3 13 2"""
        output = """3"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """10
8 6 3 9 5 4 7 2 1 10"""
        output = """1"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """14
630551244 683685976 249199599 863395255 667330388 617766025 564631293 614195656 944865979 277535591 390222868 527065404 136842536 971731491"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()