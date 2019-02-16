import asyncio
import json
from typing import List
from pprint import pprint
import datetime
from Logs import Log
import jinja2

class Maze(object):
    map: List[List[str]]
    sizeX: int
    sizeY: int

    def __init__(self, x: int = 4, y: int = 4):
        self.sizeX = x
        self.sizeY = y
        self.initMap()

    def initMap(self):
        self.map = list()
        for y in range(self.sizeY):
            self.map.append([0] * self.sizeX)
        self.map[0] = [9] + [1] * (self.sizeX - 2) + [3]
        for i in range(1, self.sizeY - 1):
            self.map[i] = [8] + [0] * (self.sizeX - 2) + [2]
        self.map[self.sizeY - 1 ] = [12] + [4] * (self.sizeX - 2) + [6]
        pprint(self.map)


if __name__ == "__main__":
    m = Maze()
    pass
