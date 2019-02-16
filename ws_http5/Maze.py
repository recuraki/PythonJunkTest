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

    def initTest(self):
        self.posStart = (0, 0)
        self.posGoal = (3, 3)
        self.map[0][0] = self.map[0][0] + 4
        self.map[0][1] = self.map[0][1] + 2

class Solver(object):
    maze: Maze
    searchCells: List[Tuple[int, int]]
    discardCells: List[Tuple[int, int]]

    def __init__(self, m: Maze):
        self.maze = m
        self.searchCells = list()
        self.discardCells = list()
        self.initTest()

    def initTest(self):
        self.discardCells.append((1, 1))
        self.discardCells.append((1, 2))
        self.searchCells.append((2, 2))
        self.searchCells.append((2, 3))

if __name__ == "__main__":
    m = Maze()
    pass
