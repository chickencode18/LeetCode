
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1,n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]




#dp
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1,n):
            for j in range(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]
'''

