import unittest
from typing import List, Dict

Queue = List[int]

import sys
import math

def list_init_elevator_location(floornum :int, elevatornum: int):
    res = []
    res.append(0)
    if elevatornum == 1:
        return res
    for i in range(elevatornum - 1):
        x = math.floor( (1/(elevatornum-1)) *  (i + 1) * floornum)
        if x == floornum:
            x -= 1
        res.append(x)

    return res

def calc_distance(destqueue: List[int], lvcur: int, lvtarget: int, dir: int) -> int:
    # e.curfloor()は切り捨ての値を返すため、upとdownは少しアルゴリズムが違う
    if len(destqueue) == 0:
        # 基本的にないパターンの場合
        return abs(lvcur - lvtarget)
    lvtmp = lvcur
    dirtmp = dir
    cost = 0
    #print("", file=sys.stderr)

    for i in range(len(destqueue)):
        cost += 1
        #print("lvtmp=currentposh{1} -> pos[{2}]{3} current cost{0}, dir={4} ".format(cost, lvtmp, i,destqueue[i], dir), file=sys.stderr)

        if dir == "up":
            if destqueue[i] < lvtmp and lvtarget <= lvtmp:
                dir = "down"
                #print("UpC-1", file=sys.stderr)
        elif dir == "down":
            if destqueue[i] > lvtmp and lvtarget >= lvtmp:
                dir = "up"
                #print("DoC-1", file=sys.stderr)


        if dir == "up":
            # 下向きになってしまった場合
            if destqueue[i] < lvtmp:
                # もし、目標がより高みであったならそれを返す
                if lvtarget > lvtmp:
                    cost += abs(lvtarget - lvtmp)
                    #print("UpA", file=sys.stderr)
                    return cost
                # そうでないなら下向きになったとみなす(で、コストを加算しないで次へ)
                cost -= 1
                dir = "down"
                #print("UpC", file=sys.stderr)
                continue
            # もし、次の目的地がターゲットを超えるのであればそこまでの距離を生産
            if destqueue[i] > lvtarget and lvcur < lvtarget:
                cost += abs(lvtarget - lvtmp)
                #print("UpB", file=sys.stderr)
                return cost
            # 単調増加中である場合、そこまでの距離を足す
            cost += abs(lvtmp - destqueue[i])
            lvtmp = destqueue[i]

        if dir == "down":
            # 上向きになった場合
            if destqueue[i] > lvtmp:
                # もし、目標がより下であったならそれを返す
                if lvtarget < lvtmp:
                    cost += abs(lvtarget - lvtmp)
                    #print("DoA", file=sys.stderr)
                    return cost
                # そうでないなら上向きになったとみなす(で、コストを加算しないで次へ)
                cost -= 1
                dir = "up"
                #print("DoC", file=sys.stderr)
                continue
            # もし、次の目的地がターゲットを超えるのであればそこまでの距離を生産
            if destqueue[i] < lvtarget and lvcur > lvtarget:
                cost += abs(lvtarget - lvtmp)
                #print("DoB", file=sys.stderr)
                return cost
            # 単調減少中である場合、そこまでの距離を足す
            cost += abs(lvtmp - destqueue[i])
            lvtmp = destqueue[i]

        if dir == "stop":
            if destqueue[i] < lvtmp:
                dir = "down"
            elif destqueue[i] > lvtmp:
                dir = "up"
            else:
                break
            cost += abs(lvtmp - destqueue[i])
            lvtmp = destqueue[i]

    cost += abs(lvtmp - lvtarget)
    # 最後の地点を出発した加算が必要
    cost += 1
    #print("finish lvtmp=currentposh{1} -> pos{2} current cost{0},  ".format(cost, lvtmp, lvtarget),
    #      file=sys.stderr)
    return cost

class TestListInitElevatorLocation(unittest.TestCase):
    def test_1(self):
        self.assertEqual(list_init_elevator_location(10, 10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(list_init_elevator_location(1,1), [0])
        self.assertEqual(list_init_elevator_location(100, 1), [0])
        self.assertEqual(list_init_elevator_location(1, 3), [0, 0, 0])
        self.assertEqual(list_init_elevator_location(10, 3), [0, 5, 9])

class TestCalcDistance(unittest.TestCase):
    def test_calc_distance_1(self):
        self.assertEqual(calc_distance([5, 6], 3, 7, "up"), 7)
    def test_calc_distance_2(self):
        self.assertEqual(calc_distance([5, 3], 6, 7, "down"), 10)
    def test_calc_distance_3(self):
        self.assertEqual(calc_distance([5, 6], 3, 2, "up"), 10)
    def test_calc_distance_4(self):
        self.assertEqual(calc_distance([5, 3], 6, 2, "down"), 7)
    def test_calc_distance_5(self):
        self.assertEqual(calc_distance([5, 6], 3, 4, "up"), 2)
    def test_calc_distance_6(self):
        self.assertEqual(calc_distance([5, 3], 6, 4, "down"), 4)
    def test_calc_distance_7(self):
        self.assertEqual(calc_distance([3, 5, 6], 4, 2, "stop"), 4)
    def test_calc_distance_8(self):
        self.assertEqual(calc_distance([5, 6, 3], 4, 2, "stop"), 10)
    def test_calc_distance_9(self):
        self.assertEqual(calc_distance([5, 6, 2 ], 3, 7, "up"), 7)
    def test_calc_distance_10(self):
        self.assertEqual(calc_distance([5, 3, 10], 6, 7, "down"), 10)


if __name__ == '__main__':
    unittest.main()
