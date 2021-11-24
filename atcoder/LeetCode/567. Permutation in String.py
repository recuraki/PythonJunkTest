class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 尺取り O(N)を狙う
        # s1の方が長ければ絶対無理

        if len(s1) > len(s2): return False
        from collections import Counter, defaultdict

        match = [0]
        target = Counter(s1)  # ほしい文字数
        cur = defaultdict(int)  # いまの範囲の文字

        def doin(x):
            # 4文字ほしい, 3o 4x
            if cur[x] < target[x]: match[0] += 1
            cur[x] += 1
            assert cur[x] >= 0

        def doout(x):
            # 4文字ほしい,なくなる。 3o 4o 5 x
            if cur[x] <= target[x]: match[0] -= 1
            cur[x] -= 1
            assert cur[x] >= 0

        for i in range(0, len(s1)):
            doin(s2[i])

        l = 0
        if match[0] == len(s1): return True

        for r in range(len(s1), len(s2)):
            doin(s2[r])
            doout(s2[l])
            l += 1
            if match[0] == len(s1): return True
        return False
