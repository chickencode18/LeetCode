
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        m = 0


        for i in range(n):
            if i > m:
                return False
            m = max(m,i+nums[i])
            if m > n-1:
                return True
            
        return True





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

