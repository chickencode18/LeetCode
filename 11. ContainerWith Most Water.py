class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1

        res = 0
        while l<r:
            w = r-l
            res = max(res,min(height[l],height[r])*w)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res
