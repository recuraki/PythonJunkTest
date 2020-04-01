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
        t = 0
        for i in range(10**9):
            t += i
            if t >= k:
                break
        t -= i
        l = i - 1
        r = k - t
        s = list("a" * n)
        s[n-2-l] = "b"
        s[n-r] = "b"
        print("".join(s))




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
        input = """9
5 1
5 2
5 8
5 10
3 1
3 2
20 100
2 1
3 3"""
        output = """aaabb
aabab
baaba
bbaaa
abb
bab
aaaaabaaaaabaaaaaaaa
bb
bba"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()