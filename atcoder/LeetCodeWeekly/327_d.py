from heapq import heappop, heappush
from collections import deque
from typing import List, Tuple, Optional


class Worker:
    def __init__(self, i, time):
        self.id = i
        self.leftToRight = time[0]
        self.pickOld = time[1]
        self.rightToLeft = time[2]
        self.putNew = time[3]

    def __lt__(self, other):  # the condition that this worker prioritized others in minimum heap.
        self.total = self.leftToRight + self.rightToLeft
        other.total = other.leftToRight + other.rightToLeft
        return self.total > other.total or (self.total == other.total and self.id > other.id)  # not less efficient.


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left_workers = []  # min heap
        right_workers = []
        left_delay_q = []
        right_delay_q = []

        # Convert workers to elements: (TotalLR time, rowNo, )
        for i, t in enumerate(time):
            left_workers.append(Worker(i, t))

        # Then, simulation
        now = 0
        dispatched = 0
        rem = n  # remaining box to finish.

        ans = 0 # LAST

        while rem > 0:
            print(left_delay_q, now)
            if left_delay_q:
                print(left_delay_q[0])
            # Consume workers from delay Q.
            while left_delay_q and len(left_delay_q) > 0 and now >= left_delay_q[0][0]:
                heappush(left_workers, heappop(left_delay_q)[1])

            while right_delay_q and len(right_delay_q) > 0 and now >= right_delay_q[0][0]:
                heappush(right_workers, heappop(right_delay_q)[1])

            if (not right_workers) and (not left_workers):  # Proceed time until the next delay queue's head.
                now = min(
                    left_delay_q[0][0] if left_delay_q else float('inf'),
                    right_delay_q[0][0] if right_delay_q else float('inf')
                )  # some worker should be either.
            elif right_workers:  # * left and * non-left
                # allow workers to cross the bridge, put box, then go to delay q.
                worker = heappop(right_workers)
                ans = max(ans, now)
                heappush(left_delay_q, (now + worker.putNew, worker))
            else:  # left_workers only:
                if rem <= 0: continue
                rem -= 1
                if dispatched >= n:  # Don't send extra person, and wait for next right side person.
                    now = right_delay_q[0][0]
                    continue
                worker = heappop(left_workers)
                now += worker.leftToRight
                dispatched += 1
                heappush(right_delay_q, (now + worker.pickOld, worker))
        print(ans)
        return ans
st = Solution()
print(st.findCrossingTime(n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]])==6)
print(st.findCrossingTime(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]])==50)
print(st.findCrossingTime(10,6,[[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]) == 149)
print(st.findCrossingTime(9, 6, [[2,6,9,4],[4,8,7,5],[4,6,7,6],[2,3,3,7],[9,3,6,8],[2,8,8,4]])== 115)