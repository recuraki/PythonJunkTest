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
        n = int(input())
        dat = list(map(int, input().split()))
        oddind = []
        evenind = []
        for i in range(n*2):
            if dat[i] % 2 == 1:
                oddind.append(i + 1)
            else:
                evenind.append(i+ 1)



        if len(oddind) % 2 == 1:
            oddind = oddind[1:]
            evenind = evenind[1:]
        elif len(oddind) == 0:
            evenind = evenind[2:]
        else:
            oddind = oddind[2:]
        for j in range(0, len(evenind), 2):
            print(evenind[j], evenind[j+1])
        for j in range(0, len(oddind), 2):
            print(oddind[j], oddind[j + 1])


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
        input = """3
3
1 2 3 4 5 6
2
5 7 9 10
5
1 3 3 4 5 90 100 101 2 3"""
        output = """3 6
4 5
3 4
1 9
2 3
4 5
6 10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()