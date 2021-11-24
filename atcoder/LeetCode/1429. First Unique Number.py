from collections import defaultdict, deque


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.cnt = defaultdict(int)
        self.q = deque([])
        for x in nums: self.add(x)

    def showFirstUnique(self) -> int:
        if len(self.q) == 0: return -1
        while len(self.q) > 0:
            x = self.q[0]
            if self.cnt[x] > 1:
                self.q.popleft()
                continue
            return x
        return -1

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        self.q.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)