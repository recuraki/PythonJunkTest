class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cum = [0] * (len(gain) + 1)
        for i in range(len(gain)): cum[i + 1] = cum[i] + gain[i]
        return max(cum)
