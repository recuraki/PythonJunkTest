import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from math import gcd
    n = int(input())
    ss = set()
    cnt = 2
    l = [3 * 5 * 7 * 11, 7 * 2]
    ss.add(3 * 5 * 7 * 11)
    ss.add(7 * 2)
    for i in range(1, 10000):
        if cnt == n:
            break
        vala = 3 * 2 * i
        if vala > 10000:
            break
        if vala not in ss:
            l.append(vala)
            ss.add(vala)
            cnt += 1
    for i in range(1, 10000):
        if cnt == n:
            break
        vala = 5 * 2 * i
        if vala > 10000:
            break
        if vala not in ss:
            l.append(vala)
            ss.add(vala)
            cnt += 1
    for i in range(1, 10000):
        if cnt == n:
            break
        vala = 7 * 2 * i
        if vala > 10000:
            break
        if vala not in ss:
            l.append(vala)
            ss.add(vala)
            cnt += 1
    for i in range(1, 10000):
        if cnt == n:
            break
        vala = 11 * 2 * i
        if vala > 10000:
            break
        if vala not in ss:
            l.append(vala)
            ss.add(vala)
            cnt += 1
    okok = True
    total = 0
    for x in l:
        total = gcd(total, x)
    assert total == 1
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            assert gcd(l[i], l[j]) != 1
    print(" ".join(list(map(str, l))))


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
        input = """4"""
        output = """84 60 105 70"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()