from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps=0
        current_end=0
        farthest=0

        for i in range(n-1):
            farthest=max(farthest,i+nums[i])

            if i==current_end:
                jumps+=1
                current_end=farthest

            if current_end>=n-1:
                break
        return jumps

#dp
'''class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(n):
            max_jump = min(n-1,i + nums[i])

            for j in range(i+1,max_jump + 1):
                 dp[j] = min(dp[j],dp[i]+1)
        return dp[-1]
'''
