class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappop, heappush
        pq = []
        from collections import defaultdict
        d = defaultdict(int)
        for x in nums: d[x] += 1
        for key in d:
            heappush(pq, (-d[key], key) )
        ans = []
        for _ in range(k):
            cnt, key = heappop(pq)
            ans.append(key)
        return ans