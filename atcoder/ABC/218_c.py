import sys
from io import StringIO
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)

def resolve():




    import sys
    input = sys.stdin.readline
    from pprint import pprint

    INF = 1 << 63
    def do():
        def judge():
            for offseth in range(n): # 全ての点
                for offsetw in range(n): # 全ての点
                    can = True
                    # そこから開始していく
                    for hh in range(n):
                        for ww in range(n):
                            # 問題ないなら続ける
                            if maze1[hh][ww] == maze2[(hh+offseth) % n][(ww+offsetw) %n]: continue
                            else:
                                # 一つでも違うなら、Falseで抜ける
                                can = False
                                break
                        # wwで一つでもダメならこのoffsetはダメなので、
                        if can is False:
                            break
                    # hh, wwが全て終わってcanなら、これで合格
                    if can: return True

            return False



        def rot(maze):
            newmaze = []
            for ww in range(n):
                s = []
                for hh in range(n):
                    s.append(maze[hh][n - ww - 1])
                newmaze.append(s)
            return newmaze
        n = int(input())
        maze1 = []
        maze2 = []

        for hh in range(n):
            l = list(input())
            buf = []
            for ww in range(n):
                x = l[ww]
                if x == ".":
                    buf.append(0)
                elif x == "#":
                    buf.append(1)
            maze1.append(buf)


        for _ in range(n):
            l = list(input())
            buf = []
            for x in l:
                if x == ".": buf.append(0)
                elif x == "#": buf.append(1)
            maze2.append(buf)

        if judge():
            print("Yes")
            return

        maze2 = rot(maze2)
        if judge():
            print("Yes")
            return

        maze2 = rot(maze2)
        if judge():
            print("Yes")
            return

        maze2 = rot(maze2)
        if judge():
            print("Yes")
            return

        maze2 = rot(maze2)
        if judge():
            print("Yes")
            return

        maze2 = rot(maze2)
        if judge():
            print("Yes")
            return

        print("No")


    do()


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
        input = """5
.....
..#..
.###.
.....
.....
.....
.....
....#
...##
....#"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_2(self):
        print("test_input_2")
        input = """5
#####
##..#
#..##
#####
.....
#####
#..##
##..#
#####
....."""
        output = """No"""
        self.assertIO(input, output)
    def test_input_3(self):
        print("test_input_3")
        input = """4
#...
..#.
..#.
....
#...
#...
..#.
...."""
        output = """Yes"""
        self.assertIO(input, output)
    def test_input_4(self):
        print("test_input_4")
        input = """4
#...
.##.
..#.
....
##..
#...
..#.
...."""
        output = """No"""
        self.assertIO(input, output)
    def test_input_41(self):
        print("test_input_41")
        input = """4
....
.#.#
....
....
....
....
....
#.#."""
        output = """Yes"""
        self.assertIO(input, output)
if __name__ == "__main__":
    unittest.main()