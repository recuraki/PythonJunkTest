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
        dat = list(map(int, input().split()))
        buf = []
        for i in range(n // 2):
            a = dat[i]
            b = dat[n - 1 - i]
            a,b = min(a,b), max(a,b)
            buf.append([a,b,a+b])
        buf.sort(key=lambda x: (x[0], x[1]))
        print(buf)

        candidate = [x[2] for x in buf]
        print(candidate)
        l = n
        h = n * k

        for i in range(len(candidate)):
            target = candidate[i][2]
            cnt = 0
            print("target", target)
            for j in range(n//2):
                print(" >j", j)
                print(" >>", buf[j])
                x, y, z = buf[j]
                diff = z - target
                print(" > diff:", diff)
                if diff == 0:
                    continue
                elif x > k and y > k:
                    cnt += 2
                    continue
                elif y > k:
                    if 1 <= (target - x) <= k:
                        cnt += 2
                    else:
                        cnt += 1
                elif diff < 0: # chiisai
                    diff = abs(diff)
                    print(" > chiisai", (k - x), ">=", diff)
                    if (k - x) >= diff:
                        print("1")
                        cnt += 1
                    else:
                        print("2")
                        cnt += 2
                elif diff > 0: # ookii
                    print(" > ookii", diff, " <", b)
                    if diff < b:
                        print("1")
                        cnt += 1
                    else:
                        print("2")
                        cnt += 2
            res = min(res, cnt)
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
        input = """4
4 2
1 2 1 2
4 3
1 2 2 1
8 7
6 1 1 7 6 3 4 6
6 6
5 2 6 1 3 4"""
        output = """0
1
4
2"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()