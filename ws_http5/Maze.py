import asyncio
import json
from typing import List
from typing import Tuple
from pprint import pprint
import datetime
from Logs import Log
import jinja2

class Maze(object):
    map: List[List[int]]
    sizeX: int
    sizeY: int
    posStart: Tuple[int, int]
    posGoal: Tuple[int, int]

    def __init__(self, x: int = 6, y: int = 6):
        self.sizeX = x
        self.sizeY = y
        self.initMap()
        self.initTest()
        pprint(self.map)

    def initMap(self):
        self.map = list()
        for y in range(self.sizeY):
            self.map.append([0] * self.sizeX)
        self.map[0] = [9] + [1] * (self.sizeX - 2) + [3]
        for i in range(1, self.sizeY - 1):
            self.map[i] = [8] + [0] * (self.sizeX - 2) + [2]
        self.map[self.sizeY - 1] = [12] + [4] * (self.sizeX - 2) + [6]

    def suggestNextPoss(self, pos: Tuple[int, int]):
        # posの位置から移動できる一覧を返す
        pprint(pos)
        r = list()
        # U
        if pos[1] != 0:
            if self.map[pos[1]][pos[0]] & 1 == 0:
                if (self.map[pos[1] - 1][pos[0]] & 4) == 0:
                    r.append((pos[0], pos[1] - 1))
        # R
        if pos[0] != (self.sizeY - 1):
            if self.map[pos[1]][pos[0]] & 2 == 0:
                if (self.map[pos[1]][pos[0] + 1] & 8) == 0:
                    r.append((pos[0] + 1, pos[1]))
        # D
        if pos[1] != (self.sizeY - 1):
            if self.map[pos[1]][pos[0]] & 4 == 0:
                if self.map[pos[1] + 1 ][pos[0]] & 1 == 0:
                    r.append((pos[0], pos[1] + 1))
        # L
        if pos[0] != 0:
            if self.map[pos[1]][pos[0]] & 8 == 0:
                if self.map[pos[1]][pos[0] - 1] & 2 == 0:
                    r.append((pos[0] - 1, pos[1]))
        return r


    def initTest(self):
        self.posStart = (0, 0)
        self.posGoal = (3, 3)
        self.map[0][0] = self.map[0][0] + 4
        self.map[0][1] = self.map[0][1] + 2
        self.map[1][1] = self.map[1][1] + 4 + 2
        self.map[2][0] = self.map[2][0] + 2
        self.map[3][0] = self.map[3][0] + 2
        self.map[4][0] = self.map[4][0] + 2
        self.map[3][3] = self.map[3][3] + 2 + 8 + 1
        self.map[4][3] = self.map[4][3] + 8 + 2
        self.map[5][3] = self.map[5][3] + 8
        self.map[2][1] = self.map[2][1] + 2
        self.map[3][1] = self.map[3][1] + 2
        self.map[4][1] = self.map[4][1] + 2
        self.map[1][2] = self.map[1][2] + 2
        self.map[0][3] = self.map[0][3] + 4
        self.map[0][4] = self.map[0][4] + 4
        self.map[0][5] = self.map[0][5] + 4


class Solver(object):
    # 枝は刈ったならDiscardに入れてかっこよく表示したい todo
    maze: Maze
    # 以下２つのメンバ変数はinit等の時に一覧ですべての探索済み等の経路を返すもの
    # 実際は@propatyで返せばいいので、後で実装しなおしましょう TODO
    searchCells: List[Tuple[int, int]]
    discardCells: List[Tuple[int, int]]
    searchMap: List[List[bool]]
    discardMap: List[List[bool]]

    def __init__(self, m: Maze):
        self.maze = m
        self.searchCells = list()
        self.discardCells = list()
        self.searchMap = list()
        self.discardMap = list()
        for y in range(self.maze.sizeY):
            self.searchMap.append([False] * self.maze.sizeX)
        self.searchMap[self.maze.posStart[1]][self.maze.posStart[0]] = True
        self.solve()



    def solve(self):
        queueSearch: List[Tuple[int, int]] = list()
        queueSearch.append(self.maze.posStart)
        while len(queueSearch) > 0 :
            pos, queueSearch = queueSearch[0], queueSearch[1:]

            print("current" + str(pos))
            for next in self.maze.suggestNextPoss(pos):
                if next == self.maze.posGoal:
                    print("SOLVED")
                    yield next,True
                if self.searchMap[next[1]][next[0]] is not False:
                    continue  # 既に動いたところには戻りたくない
                # そうでないなら次の移動候補
                self.searchMap[next[1]][next[0]] = True
                queueSearch.append(next)
                yield next,False


if __name__ == "__main__":
    m = Maze()
    pass
