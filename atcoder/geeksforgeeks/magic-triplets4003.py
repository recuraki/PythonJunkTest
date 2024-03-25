# https://practice.geeksforgeeks.org/problems/magic-triplets4003/1

#User function Template for python3
class BinaryIndexTreeSum:
    #
    # BE
    #
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
class Solution:
    def countTriplets(self, nums):
        N = 1000000
        bitLeft = BinaryIndexTreeSum(1000000)
        bitRight = BinaryIndexTreeSum(1000000)
        ans = 0
        for val in nums:
            bitLeft.add(val, 1)
        for i in range(len(nums) - 1, -1, -1):
            # center val = nums[i]
            valC = nums[i]
            numSmaller = bitLeft.sum(valC - 1)
            numGreater = bitRight.sum(N) - bitRight.sum(valC)
            #print(i, numSmaller, numGreater)
            ans += numSmaller * numGreater
            # leave this [i] val
            bitLeft.add(valC, -1)
            bitRight.add(valC, 1)
        return (ans)

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    #n = int(input())
    #nums = list(map(int,input().split()))
    n = 4
    nums = [3,1,4,1]
    nums.sort()

    ob = Solution()
    ans = ob.countTriplets(nums)
    print(ans)

# } Driver Code Ends