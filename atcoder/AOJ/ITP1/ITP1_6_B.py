import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    # 対象がN=52なので力業
    res = []
    for i in ["S", "H", "C", "D"]:
        for j in range(1, 13 + 1):
            res.append(i + " " + str(j))
    q = int(input())
    for _ in range(q):
        s = input()
        for i in range(len(res)):
            if res[i] == s:
                del res[i]
                break
    for i in range(len(res)):
        print(res[i])


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
        input = """47
S 10
S 11
S 12
S 13
H 1
H 2
S 6
S 7
S 8
S 9
H 6
H 8
H 9
H 10
H 11
H 4
H 5
S 2
S 3
S 4
S 5
H 12
H 13
C 1
C 2
D 1
D 2
D 3
D 4
D 5
D 6
D 7
C 3
C 4
C 5
C 6
C 7
C 8
C 9
C 10
C 11
C 13
D 9
D 10
D 11
D 12
D 13"""
        output = """S 1
H 3
H 7
C 12
D 8"""
        self.assertIO(input, output)

    def test_input_2(self):
        print("test_input_2")
        input = """0"""
        output = """S 1
S 2
S 3
S 4
S 5
S 6
S 7
S 8
S 9
S 10
S 11
S 12
S 13
H 1
H 2
H 3
H 4
H 5
H 6
H 7
H 8
H 9
H 10
H 11
H 12
H 13
C 1
C 2
C 3
C 4
C 5
C 6
C 7
C 8
C 9
C 10
C 11
C 12
C 13
D 1
D 2
D 3
D 4
D 5
D 6
D 7
D 8
D 9
D 10
D 11
D 12
D 13"""
        self.assertIO(input, output)

    def test_input_3(self):
        print("test_input_3")
        input = """52
S 1
S 2
S 3
S 4
S 5
S 6
S 7
S 8
S 9
S 10
S 11
S 12
S 13
H 1
H 2
H 3
H 4
H 5
H 6
H 7
H 8
H 9
H 10
H 11
H 12
H 13
C 1
C 2
C 3
C 4
C 5
C 6
C 7
C 8
C 9
C 10
C 11
C 12
C 13
D 1
D 2
D 3
D 4
D 5
D 6
D 7
D 8
D 9
D 10
D 11
D 12
D 13"""
        output = """
"""

if __name__ == "__main__":
    unittest.main()