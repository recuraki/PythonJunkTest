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

    def __init__(self, x: int = 4, y: int = 4):
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
        self.initTest()

    def initTest(self):
        self.discardCells.append((1, 1))
        self.discardCells.append((1, 2))
        self.searchCells.append((2, 2))
        self.searchCells.append((2, 3))


    def next(self):
        queueSearch: List[Tuple[int, int]] = list()
        queueSearch.append(m.posStart)
        while len(queueSearch > 0):
            pos, queueSearch = queueSearch[0], queueSearch[1:]


if __name__ == "__main__":
    m = Maze()
    pass
