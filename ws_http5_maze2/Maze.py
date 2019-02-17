import asyncio
import json
from typing import List
from typing import Tuple
from pprint import pprint
import datetime
from Logs import Log
import jinja2
import math

BLANK = 0x00
WALL = 0x01
SEARCHED = 0x02

class Maze(object):
    map: List[List[int]]
    sizeX: int
    sizeY: int
    posStart: Tuple[int, int]
    posGoal: Tuple[int, int]

    def __init__(self, x: int = 13, y: int = 13):
        self.sizeX = x
        self.sizeY = y
        self.initMap()
        self.initTest()
        pprint(self.map)

    def initMap(self):
        self.map = list()
        for y in range(self.sizeY):
            self.map.append([BLANK] * self.sizeX)
        self.map[0] = [WALL] + [WALL] * (self.sizeX - 2) + [WALL]

        for i in range(1, self.sizeY - 1):
            if i % 2 == 1:
                self.map[i] = [WALL] + [0] * (self.sizeX - 2) + [WALL]
            else:
                self.map[i] = [WALL] + [0, 1] * math.ceil((self.sizeX - 2) / 2)


        self.map[self.sizeY - 1] = [WALL] + [WALL] * (self.sizeX - 2) + [WALL]

    def suggestNextPoss(self, pos: Tuple[int, int]):
        # posの位置から移動できる一覧を返す
        pprint(pos)
        r = list()
        # U
        if pos[1] != 0:
            if self.getMap(pos[0], pos[1] - 1) & WALL == 0:
                r.append((pos[0], pos[1] - 1))
        # R
        if pos[0] != (self.sizeY - 1):
            if self.getMap(pos[0] + 1, pos[1]) & WALL == 0:
                r.append((pos[0] + 1, pos[1]))
        # D
        if pos[1] != (self.sizeY - 1):
            if self.getMap(pos[0], pos[1] + 1) & WALL == 0:
                r.append((pos[0], pos[1] + 1))
        # L
        if pos[0] != 0:
            if self.getMap(pos[0] - 1, pos[1]) & WALL == 0:
                r.append((pos[0] - 1, pos[1]))
        return r

    def setWall(self, x, y):
        self.map[y][x] = self.map[y][x] | WALL

    def getMap(self, x, y):
        return self.map[y][x]

    def initTest(self):
        self.posStart = (1, 1)
        self.posGoal = (7, 7)
        self.setWall(1,2)
        self.setWall(4, 1)
        self.setWall(4, 1)
        self.setWall(2, 5)
        self.setWall(2, 7)
        self.setWall(2, 9)
        self.setWall(4, 3)
        self.setWall(3, 4)
        self.setWall(4, 5)
        self.setWall(4, 7)
        self.setWall(4, 9)
        self.setWall(6, 3)
        self.setWall(6, 7)
        self.setWall(6, 9)
        self.setWall(6, 11)
        self.setWall(7, 2)
        self.setWall(9, 2)
        self.setWall(11, 2)
        self.setWall(7, 6)
        self.setWall(8, 7)
        self.setWall(8, 9)

        pprint(self.suggestNextPoss((1,1)))


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
