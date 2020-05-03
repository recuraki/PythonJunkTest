import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    import sys
    def dprint(s):
        #pprint(s)
        pass

    q = int(input())
    import collections
    for _ in range(q):
        #print("---")
        n, k = map(int, input().split())
        s = input()
        dat = list(s)
        dat.sort()
        #print(dat)
        if k == 1:
            print("".join(dat))
        else:
            isfinish = False
            dat = collections.deque(dat)
            res = []
            while len(dat) >= k:
                issame = True
                first = dat.popleft()
                dprint("while res = {0}".format(res))
                dprint("first:" + str(first))
                for i in range(k - 1):
                    next = dat.popleft()
                    dprint(" > for" + str(i) + ":" +str(next))
                    if next == first:
                        continue
                    else:
                        dprint(" >> diffrent")
                        res.append(next)
                        isfinish = True
                        issame = False
                        break

                if isfinish:
                    dprint(" >> isfinish")
                    break

                if len(res) == 0:
                    res.append(next)
                elif len(dat) == 0 and issame is True:
                    res.append(first)
                else:
                    ne = dat.popleft()
                    dat.appendleft(ne)
                    if ne == first:
                        res.append(first)
                    else:
                        for i in range(k):
                            res.append(first)

            dprint("loop end dat=" + str(dat) + " res=" + str(res))
            dprint(str(res) + str(issame))
            if len(dat) > 0 and issame is True:
                res.append(dat.pop())
            dprint(str(res))
            print("".join(res))

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
10 3
aaaaaaaaaa"""
        output = """a"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_1")
        input = """1
10 3
aaaaaaaaaa"""
        output = """a"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()