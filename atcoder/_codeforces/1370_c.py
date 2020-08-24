import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if arr == []:
            arr.append([n, 1])
        return arr

    from pprint import pprint
    import sys

    msgf = "FastestFinger"
    msga = "Ashishgup"

    q = int(input())
    for _ in range(q):
        n = int(input())
        if n == 1:
            print(msgf)
            continue
        if n == 2:
            print(msga)
            continue
        if n % 2 == 1:
            print(msga)
            continue
        l = factorization(n)
        #print(l)
        oddcnt = 0
        evencnt = 0
        for num, cnt in l:
            if num % 2 == 1:
                oddcnt += cnt
            else:
                evencnt += cnt

        if oddcnt == 0:
            print(msgf)
            continue
        if oddcnt == 1 and evencnt == 1:
            print(msgf)
        else:
            print(msga)





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
        input = """7
1
2
3
4
5
6
100"""
        output = """FastestFinger
Ashishgup
Ashishgup
FastestFinger
Ashishgup
FastestFinger
Ashishgup"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()