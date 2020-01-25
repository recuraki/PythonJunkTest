import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():
    from pprint import pprint
    n, q = map(int, input().split())
    import bisect
    maze = []
    numreason = 0

    for _ in range(n+2):
        maze.append([0,0,0,0])

    def isabovefloorcandown(fnum):
        if maze[fnum-1][1] == 0 and maze[fnum][1] == 0:
            return True
        if maze[fnum-1][2] == 0 and maze[fnum][2] == 0:
            return True
        return False

    def isdownfloorcandown(fnum):
        if maze[fnum+1][1] == 0 and maze[fnum][1] == 0:
            return True
        if maze[fnum+1][2] == 0 and maze[fnum][2] == 0:
            return True
        return False

    for qq in range(q):
        #pprint(maze)
        r, c = map(int, input().split())
        #print("r,c{0}{1}".format(r,c))
        r = r

        scur = isabovefloorcandown(c)
        scurd = isdownfloorcandown(c)
        maze[c][r] = 1 if maze[c][r] == 0 else 0
        safter = isabovefloorcandown(c)
        safterd = isdownfloorcandown(c)
        if scur is True and safter is False:
            numreason += 1
        elif scur is False and safter is True:
            numreason -= 1

        if scurd is True and safterd is False:
            numreason += 1
        elif scurd is False and safterd is True:
            numreason -= 1


        print("Yes" if numreason == 0 else "No")

    #pprint(maze)

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
        input = """5 5
2 3
1 4
2 4
2 3
1 4"""
        output = """Yes
No
No
No
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()