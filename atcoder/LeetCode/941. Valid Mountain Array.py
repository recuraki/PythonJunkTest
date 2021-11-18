class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        O(N)で単調増加と単調増加(厳密に)
        ==は無視して良さそう
        O(logN)でも解けそう。
        ⇒嘘。でこぼこがある場合、2文探索できない

        コーナーケース考える。
        [0,1,0]
        [0,1,1,0]

        WA: あ、両端が0じゃないのか。
        """

        # とりあえずO(N)
        if len(arr) < 3: return False
        candidate = 0
        for i in range(1, len(arr) - 1):  # 0<->0で00は探索しない
            if arr[i - 1] < arr[i]:
                candidate = i
                continue
            break
        # == のノードがあるときは次ではじけるので気にしない
        print(candidate)
        for i in range(candidate, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                continue
            return False
        print(candidate)
        if 0 < candidate < len(arr) - 1: return True
        return False
