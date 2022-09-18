from typing import List, Tuple
from pprint import pprint


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        import copy
        onums = copy.deepcopy(nums)

        nums = []
        for x in onums:
            if x >= 0: nums.append(x)
        nums.sort(reverse=True)
        candidate = []
        ma = min(18, len(nums))
        for pat in range(2**ma):
            num = 0
            for i in range(ma):
                if ((pat >> i)&1) == 1:
                    num += nums[i]
            candidate.append(num)

        candidate2 = []
        nums = []
        for x in onums:
            if x < 0: nums.append(x)
        nums.sort()
        ma = min(18, len(nums))
        for pat in range(1, 2**ma):
            num = 0
            for i in range(ma):
                if ((pat >> i)&1) == 1:
                    num += nums[i]
            candidate2.append(num)
        for i in range(min(18, len(nums)), min(18, len(nums))):
            candidate2.append(num)
        #print(candidate)
        #print(candidate2)
        candidate3 = []
        candidate.sort(reverse=True)
        candidate2.sort(reverse=True)
        for x in candidate[:2010]:
            candidate3.append(x)
            for y in candidate2[:2010]:
                candidate3.append(x + y)

        candidate3.sort(reverse=True)
        #print(len(candidate))
        #print(len(candidate2))
        #print(len(candidate3))
        #print(candidate3[k-1])
        return(candidate3[k-1])




st = Solution()

print(st.kSum(nums = [2,4,-2], k = 5)==2)
print(st.kSum(nums = [1,-2,3,4,-10,12], k = 16)==10)
print(st.kSum([-487322177,-656480132,850198596,-291605661,-272668395,110865952,-162529283,-145886963,202657909,125667049,-282090943,120877054,-85849348,-482630078,-802177895,-574862206,374637017,804297842],1707)== 1493582115)
print(st.kSum([-347135403,-741775723,349271195,967839234,822470265,-545249891,293401682,908306445,296832265,9392523,-84929173,-784997375,699878100,291656873,-910458294,547370160,584504507,977373244,-963031162,819184328],473)==6283116088)
print(st.kSum([153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943,746632801,500370163,164413366,346449701,473890512]
, 1906)==5133036302)
