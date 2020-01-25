import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    h, w = map(int, input().split())
    dat = []
    for i in range(h):
        dat.append(input())

    def find_black(x,y):
        m_x = [ 0, 1,0,-1]
        m_y = [-1,0,1,0]
        #print("{0},{1}: come".format(x, y))

        for ii in range(len(m_x)):
            nx, ny = (x + m_x[ii]), (y + m_y[ii])
            #print("is black:{0},{1} = # {2},{3}".format(nx, ny, w,h ))
            if (0 <= nx < w) and (0 <= ny < h):
                if dat[ny][nx] == "#":
                    #print("YES")
                    return True
        return False

    c = True
    for i in range(h):
        for j in range(w):
            if dat[i][j] == "#":
                #print("{0},{1} = #".format(j, i))
                if find_black(j, i) is False:
                    c = False

    print("Yes" if c else "No")



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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()