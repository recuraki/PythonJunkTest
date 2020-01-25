
import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    q = int(input())
    import collections
    for qq in range(q):
        n = int(input())
        dat = list(map(int, input().split()))
        c = collections.Counter(dat)
        #print(c)
        can = True
        l = []
        for k in c:
            #print(k)
            if (c[k] % 2) != 0:
                #print("no count!")
                can = False
            for j in range(c[k] // 2):
                l.append(k)

        if can is False:
            print("NO")
            continue
        l.sort()
        l = collections.deque(l)
        #print(l)

        menseki = l.pop() * l.popleft()
        for i in range( n - 1):
            #print("Try:{0}".format(i))
            t = l.pop() * l.popleft()
            if t != menseki:
                can = False

        print("YES" if can else "NO")






class TestClass(unittest.TestCase):
    maxDiff = 100000
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
1
1 1 10 9
2
10 5 2 10 1 1 2 5
4
10 5 1 10 5 1 1 1 1 1 1 1 1 1 1 1
2
1 1 1 1 1 1 1 1
1
10000 10000 10000 10000"""
        output = """NO
YES
NO
YES
YES"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()