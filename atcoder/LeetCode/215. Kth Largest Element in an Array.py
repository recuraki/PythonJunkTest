class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop
        pq = []
        for x in nums: heappush(pq, -x)
        for _ in range(k): ans = heappop(pq)
        return -ans
