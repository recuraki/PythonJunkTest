from typing import List, Tuple
from pprint import pprint

import collections
from heapq import  heappop, heappush, heapify

hashVideo = lambda shop, movie: shop * (10 ** 10) + movie
from copy import deepcopy

class MovieRentingSystem():
    videoPrice = []
    allVideoByCost = []
    searchTable = []
    delTableallVideoByCost = collections.defaultdict(int)
    delTablesearchTable = collections.defaultdict(int)
    def __init__(self, n: int, entries: List[List[int]]):
        self.videoPrice = []
        self.allVideoByCost = []
        self.searchTable = []
        self.delTableallVideoByCost = collections.defaultdict(int)
        self.delTablesearchTable = collections.defaultdict(int)
        # videoPride[shopnum][video] = Price
        self.videoPrice = [collections.defaultdict(int) for _ in range(n)]
        self.searchTable = [[] for _ in range(10000 + 10)]

        for shop, movie,price in entries:
            self.videoPrice[shop][movie] = price

            x = (price, shop)
            heappush(self.searchTable[movie], x)


    def search(self, movie: int) -> List[int]:
        res = []
        buffer = []
        while len(self.searchTable[movie]) > 0:
            if len(res) == 5: break
            x = heappop(self.searchTable[movie])
            price, shop = x
            h = hashVideo(shop, movie)
            if self.delTablesearchTable[h] > 0:
                self.delTablesearchTable[h] -= 1
                continue
            buffer.append(x)
            res.append(shop)
        for x in buffer:
            heappush(self.searchTable[movie], x)
        return deepcopy(res)

    def rent(self, shop: int, movie: int) -> None:
        price = self.videoPrice[shop][movie]
        self.delTablesearchTable[hashVideo(shop,movie)] += 1

        x = (price, shop, movie)
        heappush(self.allVideoByCost, x)

    def drop(self, shop: int, movie: int) -> None:
        price = self.videoPrice[shop][movie]

        self.delTableallVideoByCost[hashVideo(shop, movie)] += 1

        x = (price, shop)
        heappush(self.searchTable[movie], x)

    def report(self) -> List[List[int]]:
        res = []
        buffer = []
        print("---")
        while len(self.allVideoByCost) > 0:
            if len(res) == 5: break
            x = heappop(self.allVideoByCost)
            print(">", x)
            price, shop, movie = x
            h = hashVideo(shop, movie)
            if self.delTableallVideoByCost[h] > 0:
                self.delTableallVideoByCost[h] -= 1
                continue
            buffer.append(x)
            print(x)
            res.append([shop, movie])
        for x in buffer:
            heappush(self.allVideoByCost, x)
        return deepcopy(res)


